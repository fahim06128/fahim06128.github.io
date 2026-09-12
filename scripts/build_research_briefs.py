import os
import re
import pathlib
import subprocess
import pypdf

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

def find_browser():
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    raise FileNotFoundError("Could not find Chrome or Edge executable.")

def md_to_html(md_text):
    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', md_text, flags=re.DOTALL)
    lines = text.strip().split('\n')
    
    title = ""
    meta_lines = []
    sections = []
    current_sec = None

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        
        if line.startswith('# ') and not title:
            title = line[2:].strip()
        elif line.startswith('**Author:**') or line.startswith('**Supervisor:**') or line.startswith('**Affiliation:**') or line.startswith('**Degree:**') or line.startswith('**Status:**'):
            meta_lines.append(line)
        elif line.startswith('## '):
            if current_sec:
                sections.append(current_sec)
            current_sec = {'heading': line[3:].strip(), 'items': []}
        elif line.startswith('- ') or line.startswith('* '):
            item_text = line[2:].strip()
            if current_sec:
                if current_sec['items'] and current_sec['items'][-1][0] == 'ul':
                    current_sec['items'][-1][1].append(item_text)
                else:
                    current_sec['items'].append(('ul', [item_text]))
        else:
            if current_sec:
                current_sec['items'].append(('p', line))
    
    if current_sec:
        sections.append(current_sec)
    
    def format_inline(s):
        s = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'\*(.*?)\*', r'<em>\1</em>', s)
        return s

    html_parts = []
    html_parts.append('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<style>')
    html_parts.append('''
      @page {
        size: letter;
        margin: 0.42in 0.52in 0.38in 0.52in;
      }
      * { box-sizing: border-box; }
      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        color: #1a202c;
        margin: 0;
        padding: 0;
        background: #fff;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }
      .brief-header {
        border-bottom: 2px solid #0b2f4c;
        padding-bottom: 5px;
        margin-bottom: 7px;
      }
      .brief-tag {
        font-size: 7.5pt;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #0284c7;
        margin-bottom: 2px;
      }
      h1 {
        font-size: 13.5pt;
        font-weight: 700;
        color: #071827;
        line-height: 1.22;
        margin: 0 0 5px 0;
      }
      .brief-meta {
        font-size: 7.8pt;
        color: #475569;
        line-height: 1.35;
      }
      .brief-meta strong {
        color: #0f172a;
      }
      .brief-meta div {
        margin-bottom: 1px;
      }
      h2 {
        font-size: 8.8pt;
        font-weight: 700;
        color: #0b2f4c;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        border-bottom: 0.5px solid #cbd5e1;
        padding-bottom: 1px;
        margin-top: 6px;
        margin-bottom: 3px;
      }
      p {
        font-size: 8.1pt;
        line-height: 1.32;
        color: #1e293b;
        margin: 0 0 4px 0;
        text-align: justify;
      }
      ul {
        margin: 2px 0 4px 14px;
        padding: 0;
      }
      li {
        font-size: 8.0pt;
        line-height: 1.30;
        color: #1e293b;
        margin-bottom: 2px;
      }
      strong {
        font-weight: 600;
        color: #0f172a;
      }
      .brief-footer {
        border-top: 0.5px solid #cbd5e1;
        margin-top: 7px;
        padding-top: 3px;
        font-size: 7.0pt;
        color: #64748b;
        display: flex;
        justify-content: space-between;
      }
    ''')
    html_parts.append('</style>\n</head>\n<body>\n')
    
    html_parts.append('<div class="brief-header">')
    html_parts.append('  <div class="brief-tag">Academic Research Brief &bull; Md. Fahim</div>')
    html_parts.append(f'  <h1>{format_inline(title)}</h1>')
    html_parts.append('  <div class="brief-meta">')
    for m in meta_lines:
        html_parts.append(f'    <div>{format_inline(m)}</div>')
    html_parts.append('  </div>')
    html_parts.append('</div>')
    
    for sec in sections:
        html_parts.append(f'<h2>{format_inline(sec["heading"])}</h2>')
        for item_type, content in sec['items']:
            if item_type == 'p':
                html_parts.append(f'<p>{format_inline(content)}</p>')
            elif item_type == 'ul':
                html_parts.append('<ul>')
                for li in content:
                    html_parts.append(f'<li>{format_inline(li)}</li>')
                html_parts.append('</ul>')
    
    html_parts.append('<div class="brief-footer">')
    html_parts.append('  <span>Bangladesh University of Engineering and Technology (BUET)</span>')
    html_parts.append('  <span>Academic Research Summary &bull; 1 of 1</span>')
    html_parts.append('</div>')
    html_parts.append('</body>\n</html>')
    
    return '\n'.join(html_parts)

def compile_brief(md_file, output_pdf):
    browser = find_browser()
    md_path = pathlib.Path(md_file).resolve()
    pdf_path = pathlib.Path(output_pdf).resolve()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    html_content = md_to_html(md_text)
    temp_html = pdf_path.with_suffix('.temp.html')
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        temp_html.as_uri()
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if temp_html.exists():
        temp_html.unlink()
        
    if res.returncode != 0:
        raise RuntimeError(f"Browser PDF generation failed: {res.stderr}")
    
    reader = pypdf.PdfReader(str(pdf_path))
    num_pages = len(reader.pages)
    print(f"Generated: {output_pdf} | Pages: {num_pages} | Size: {pdf_path.stat().st_size} bytes")
    if num_pages != 1:
        print(f"  [WARNING] Expected 1 page, got {num_pages} pages!")
    return num_pages

if __name__ == '__main__':
    print("=== Compiling Research Brief PDFs ===")
    p1 = compile_brief("research-briefs/thesis-research-brief.md", "assets/pdf/research/thesis-research-brief.pdf")
    p2 = compile_brief("research-briefs/nilm-wtal-research-brief.md", "assets/pdf/research/nilm-wtal-research-brief.pdf")
    if p1 == 1 and p2 == 1:
        print("\nSUCCESS: Both research briefs compiled to exactly 1 page!")
    else:
        print("\nFinished with warnings: check page counts.")
