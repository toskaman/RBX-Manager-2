import os
import sys
import re
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_config():
    config_path = os.path.join(ROOT, '_config.yml')
    assert os.path.exists(config_path), "_config.yml missing"
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'url: "https://toskaman.github.io"' in content, "Missing or wrong url in _config.yml"
    assert 'baseurl: "/RBX-Manager-2"' in content, "Missing or wrong baseurl in _config.yml"
    assert 'jekyll-sitemap' in content, "Missing jekyll-sitemap in _config.yml"
    assert 'jekyll-seo-tag' in content, "Missing jekyll-seo-tag in _config.yml"
    print("PASS: _config.yml verification")

def test_robots():
    robots_path = os.path.join(ROOT, 'robots.txt')
    assert os.path.exists(robots_path), "robots.txt missing"
    with open(robots_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'Sitemap: https://toskaman.github.io/RBX-Manager-2/sitemap.xml' in content, "Invalid sitemap in robots.txt"
    assert 'OAI-SearchBot' in content, "OAI-SearchBot not handled in robots.txt"
    print("PASS: robots.txt verification")

def test_jsonld():
    head_path = os.path.join(ROOT, '_includes', 'head.html')
    assert os.path.exists(head_path), "head.html missing"
    with open(head_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract script ld+json
    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    assert match, "JSON-LD script tag missing in head.html"
    raw_json = match.group(1).strip()
    
    # Clean liquid tags for JSON parsing test
    cleaned_json = re.sub(r'\{\{.*?\}\}', 'https://toskaman.github.io/RBX-Manager-2/', raw_json)
    cleaned_json = re.sub(r'\{%.*?%\}', '', cleaned_json)
    
    data = json.loads(cleaned_json)
    assert "@context" in data and data["@context"] == "https://schema.org", "Invalid @context in JSON-LD"
    assert "@graph" in data, "@graph missing in JSON-LD"
    
    types = [item.get("@type") for item in data["@graph"]]
    for req_type in ("SoftwareApplication", "WebSite", "WebPage", "Organization", "BreadcrumbList", "FAQPage"):
        assert req_type in types, f"{req_type} missing from @graph"
    
    for item in data["@graph"]:
        if item.get("@type") == "SoftwareApplication":
            assert item.get("operatingSystem"), "operatingSystem missing in SoftwareApplication"
            assert item.get("offers"), "offers missing in SoftwareApplication"
            assert "price" in item["offers"], "price missing in offers"
            assert item.get("downloadUrl"), "downloadUrl missing in SoftwareApplication"
    print("PASS: JSON-LD multi-entity graph validation (SoftwareApplication, WebSite, WebPage, Organization, BreadcrumbList, FAQPage)")

def test_hreflang():
    head_path = os.path.join(ROOT, '_includes', 'head.html')
    with open(head_path, 'r', encoding='utf-8') as f:
        content = f.read()
    expected_langs = ['x-default', 'en', 'es', 'pt-BR', 'fr', 'de']
    for lang in expected_langs:
        pattern = f'hreflang="{lang}"'
        assert pattern in content, f"hreflang {lang} missing in head.html"
    print("PASS: Hreflang bidirectional annotations validation")

def test_localized_pages():
    pages = [
        ('es/index.md', 'es', '/es/'),
        ('pt-br/index.md', 'pt-BR', '/pt-br/'),
        ('fr/index.md', 'fr', '/fr/'),
        ('de/index.md', 'de', '/de/')
    ]
    for rel_path, expected_lang, expected_perm in pages:
        full_path = os.path.join(ROOT, rel_path)
        assert os.path.exists(full_path), f"Localized page missing: {rel_path}"
        with open(full_path, 'r', encoding='utf-8') as f:
            c = f.read()
        assert f"lang: {expected_lang}" in c, f"Wrong lang in {rel_path}"
        assert f"permalink: {expected_perm}" in c, f"Wrong permalink in {rel_path}"
        assert c.count('class="faq-item"') >= 6, f"Expected >= 6 FAQ items in {rel_path}"
        assert c.count('class="cyber-table"') >= 2, f"Expected >= 2 comparison tables in {rel_path}"
    print("PASS: Localized pages full content & structure validation (es, pt-br, fr, de)")

def test_favicon_manifest_404():
    favicon_path = os.path.join(ROOT, 'assets', 'images', 'favicon.svg')
    manifest_path = os.path.join(ROOT, 'site.webmanifest')
    page404_path = os.path.join(ROOT, '404.html')
    assert os.path.exists(favicon_path), "favicon.svg missing"
    assert os.path.exists(manifest_path), "site.webmanifest missing"
    assert os.path.exists(page404_path), "404.html missing"
    with open(manifest_path, 'r', encoding='utf-8') as f:
        m = json.load(f)
    assert m.get("name") == "RBX Manager 2", "Invalid name in site.webmanifest"
    with open(page404_path, 'r', encoding='utf-8') as f:
        p404 = f.read()
    assert "permalink: /404.html" in p404, "Missing permalink: /404.html in 404.html"
    assert "noindex: true" in p404, "Missing noindex: true in 404.html"
    print("PASS: Favicon SVG, Web App Manifest, and Custom 404.html validation")

def test_readme_credibility():
    readme_path = os.path.join(ROOT, 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        c = f.read()
    assert "100% safe" not in c.lower() or "safe (native duplicatehandle)" in c.lower(), "Unqualified '100% safe' claim found in README"
    assert "The #1 Next-Gen" not in c, "'#1 Next-Gen' unverified claim found in README"
    assert "0 bans" not in c.lower(), "Unqualified '0 bans' guarantee found in README"
    assert "toskaman.github.io/RBX-Manager-2" in c, "Link to official showcase missing in README"
    assert "https://discord.gg/zNpj8ctH9p" in c, "Discord link missing in README"
    print("PASS: README credibility and verified claims audit")

def main():
    print("--- RUNNING SEO & REPO TEST SUITE ---")
    test_config()
    test_robots()
    test_jsonld()
    test_hreflang()
    test_localized_pages()
    test_favicon_manifest_404()
    test_readme_credibility()
    print("--- ALL 7 TEST SUITES PASSED (100% SUCCESS) ---")

if __name__ == '__main__':
    main()
