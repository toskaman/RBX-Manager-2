#!/usr/bin/env python3
"""
IndexNow Instant Search Engine Indexing Submitter for RBX-Manager-2
Pings https://api.indexnow.org/indexnow with the updated URLs and verification key.

Specification: https://www.indexnow.org/documentation
Payload fields: host, key, keyLocation, urlList
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_HOST = "toskaman.github.io"
DEFAULT_KEY = "e7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
DEFAULT_KEY_LOCATION = "https://toskaman.github.io/RBX-Manager-2/e7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2.txt"
DEFAULT_ENDPOINT = "https://api.indexnow.org/indexnow"

DEFAULT_URLS = [
    "https://toskaman.github.io/RBX-Manager-2/",
    "https://toskaman.github.io/RBX-Manager-2/es/",
    "https://toskaman.github.io/RBX-Manager-2/pt-br/",
    "https://toskaman.github.io/RBX-Manager-2/fr/",
    "https://toskaman.github.io/RBX-Manager-2/de/",
]

def get_local_key():
    key_file = os.path.join(ROOT, f"{DEFAULT_KEY}.txt")
    if os.path.exists(key_file):
        with open(key_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return DEFAULT_KEY

def build_payload(host, key, key_location, url_list):
    # Validate payload
    if not host:
        raise ValueError("Host cannot be empty")
    if not key:
        raise ValueError("Key cannot be empty")
    if not url_list or not isinstance(url_list, list):
        raise ValueError("urlList must be a non-empty list")
    for u in url_list:
        if not u.startswith("http://") and not u.startswith("https://"):
            raise ValueError(f"Invalid URL in urlList: {u}")
        if host not in u:
            raise ValueError(f"URL does not belong to host {host}: {u}")

    payload = {
        "host": host,
        "key": key,
        "keyLocation": key_location,
        "urlList": url_list
    }
    return payload

def submit_indexnow(payload, endpoint=DEFAULT_ENDPOINT, timeout=15):
    data_bytes = json.dumps(payload, indent=2).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=data_bytes,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "RBX-Manager-2-SEO-Bot/1.0"
        },
        method="POST"
    )

    print(f"Submitting {len(payload['urlList'])} URLs to IndexNow ({endpoint})...")
    print(f"Host: {payload['host']}")
    print(f"Key: {payload['key']}")
    print(f"Key Location: {payload['keyLocation']}")

    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            status_code = response.getcode()
            body = response.read().decode("utf-8", errors="replace")
            print(f"\n[SUCCESS] Response HTTP {status_code}")
            if status_code in (200, 202):
                if status_code == 200:
                    print("IndexNow status: 200 OK — URLs successfully submitted.")
                else:
                    print("IndexNow status: 202 Accepted — URLs queued; key verification pending.")
            if body:
                print(f"Response body: {body}")
            return status_code, body
    except urllib.error.HTTPError as err:
        status_code = err.code
        body = err.read().decode("utf-8", errors="replace")
        print(f"\n[HTTP ERROR] Response HTTP {status_code}: {err.reason}")
        if status_code == 403:
            print("Note: HTTP 403 Forbidden indicates that the key file is not yet verified or reachable.")
            print("If this is running immediately after a commit push, GitHub Pages deployment may still be pending.")
        elif status_code == 422:
            print("Note: HTTP 422 Unprocessable Entity — check host and URL consistency.")
        elif status_code == 429:
            print("Note: HTTP 429 Too Many Requests — rate limit encountered.")
        if body:
            print(f"Response body: {body}")
        return status_code, body
    except urllib.error.URLError as err:
        print(f"\n[NETWORK ERROR] Failed to connect to IndexNow: {err.reason}")
        return None, str(err.reason)

def main():
    parser = argparse.ArgumentParser(description="Submit updated URLs to IndexNow API")
    parser.add_argument("--dry-run", action="store_true", help="Print payload without sending HTTP request")
    parser.add_argument("--key", default=os.getenv("INDEXNOW_KEY", get_local_key()), help="IndexNow verification key")
    parser.add_argument("--host", default=os.getenv("INDEXNOW_HOST", DEFAULT_HOST), help="Host domain")
    parser.add_argument("--key-location", default=os.getenv("INDEXNOW_KEY_LOCATION", DEFAULT_KEY_LOCATION), help="Full URL to key file")
    parser.add_argument("--endpoint", default=os.getenv("INDEXNOW_ENDPOINT", DEFAULT_ENDPOINT), help="IndexNow API endpoint")
    parser.add_argument("--urls", nargs="*", default=DEFAULT_URLS, help="List of URLs to submit")
    parser.add_argument("--strict", action="store_true", help="Exit with non-zero status code on HTTP error (e.g., 403 pending deploy)")

    args = parser.parse_args()

    payload = build_payload(args.host, args.key, args.key_location, args.urls)

    if args.dry_run:
        print("=== INDEXNOW PAYLOAD (DRY RUN) ===")
        print(json.dumps(payload, indent=2))
        print("Dry run completed successfully. Payload is valid.")
        sys.exit(0)

    status_code, body = submit_indexnow(payload, endpoint=args.endpoint)

    if status_code in (200, 202):
        print("\nIndexNow submission completed successfully.")
        sys.exit(0)
    elif status_code == 403 and not args.strict:
        # In CI, 403 occurs if GitHub Pages has not finished publishing the key file yet.
        print("\nIndexNow received request (Key validation pending live deployment). Continuing.")
        sys.exit(0)
    else:
        print(f"\nIndexNow submission concluded with status: {status_code}")
        if args.strict:
            sys.exit(1)
        sys.exit(0)

if __name__ == "__main__":
    main()
