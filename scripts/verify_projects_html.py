import os, re

html_path = '_site/projects/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all <a> tags with class containing project-btn
a_tags = re.findall(r'<a\s+[^>]*class="[^"]*project-btn[^"]*"[^>]*>', html)
print('Total anchor buttons found:', len(a_tags))
for tag in a_tags:
    href_match = re.search(r'href="([^"]+)"', tag)
    if href_match:
        href = href_match.group(1)
        if href.startswith('http'):
            print('  External link:', href)
        else:
            rel = href.replace('/al-folio/', '')
            site_file = os.path.join('_site', rel)
            exists = os.path.exists(site_file)
            print('  Internal link:', rel, '->', 'EXISTS' if exists else 'MISSING')

# Also check button elements for video demo
btn_tags = re.findall(r'<button\s+[^>]*class="[^"]*project-btn[^"]*"[^>]*>', html)
print('Total button elements (video modals):', len(btn_tags))
for b in btn_tags:
    print('  Button:', b)
