import glob
import os
import re
from markdown import markdown

# Find all markdown files recursively
md_files = glob.glob('**/*.md', recursive=True)

# Map note names to unique IDs for internal links
note_to_id = {}
for file in md_files:
    note_name = os.path.splitext(os.path.basename(file))[0]
    note_id = note_name.lower().replace(' ', '-')
    note_to_id[note_name] = note_id

# Function to replace Obsidian internal links
def replace_internal_links(md_content):
    def replacer(match):
        link_text = match.group(1).strip()
        if '|' in link_text:
            note_name, display_text = link_text.split('|', 1)
            note_name = note_name.strip()
            display_text = display_text.strip()
        else:
            note_name = display_text = link_text
        return f'<a href="#{note_to_id.get(note_name, link_text)}">{display_text}</a>' if note_name in note_to_id else match.group(0)
    return re.sub(r'\[\[(.*?)\]\]', replacer, md_content)

# Process each markdown file
html_sections = []
for file in md_files:
    with open(file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    # Replace internal links
    md_content = replace_internal_links(md_content)
    # Convert to HTML
    html_content = markdown(md_content)
    # Use first heading as title, or file name if no heading
    note_name = os.path.splitext(os.path.basename(file))[0]
    heading_match = re.search(r'^#\s+(.*)', md_content, re.MULTILINE)
    title = heading_match.group(1) if heading_match else note_name
    section_id = note_to_id[note_name]
    html_sections.append((section_id, title, f'<section id="{section_id}"><h1>{title}</h1>{html_content}</section>'))

# Generate table of contents
toc = '<ul>' + ''.join(f'<li><a href="#{sid}">{title}</a></li>' for sid, title, _ in html_sections) + '</ul>'

# Combine sections
combined_html = '\n'.join(section for _, _, section in html_sections)

# HTML template with Bootstrap
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Obsidian Notes</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.3/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Table of Contents</h1>
        {toc}
        {combined_html}
    </div>
</body>
</html>"""

# Write output
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html_template)
