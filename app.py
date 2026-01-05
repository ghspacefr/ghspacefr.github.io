import re
import os

import yaml

from datetime import datetime
from markdown import markdown
from jinja2 import Environment, FileSystemLoader

from scripts.generate_index_pages import generate_index_pages_for_directory

CONTENT_DIR         = os.environ.get('CONTENT_DIR', 'content')
TEMPLATE_DIR        = os.environ.get('TEMPLATE_DIR', 'template')
PUBLIC_DIR          = os.environ.get('PUBLIC_DIR', 'public')
STATIC_DIR          = os.environ.get('STATIC_DIR', 'static')
BASE_TEMPLATE       = os.environ.get('BASE_TEMPLATE', 'base.html')
CONFIG_FILE         = os.environ.get('CONFIG_FILE', 'config.yaml')

def fread(path : str) -> str:
    with open(path, "r") as f: return f.read()

def fwrite(path : str, data) -> str:
    with open(path, "w") as f: return f.write(data)

def fm_load(path: str) -> dict:
    content = fread(path)
    pattern = re.compile(r'^---\s*(.*?)\s*---', re.DOTALL)
    match = pattern.search(content)
    if match:
        fm_content = match.group(1)
        fm_dict = yaml.safe_load(fm_content)
        fm_dict.setdefault("template", BASE_TEMPLATE)
        fm_dict.setdefault("last_update", datetime.fromtimestamp(
            os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S'))
        fm_dict["content"] = content[match.end():] 
        fm_dict["url"] = os.path.normpath(
            os.path.relpath(path.replace(".md", ".html"), CONTENT_DIR))
        print(fm_dict)
        return fm_dict
    else:
        return {}

def f_markdown(data):
    return markdown(data, extensions=['attr_list', 'fenced_code'])

def g_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():

    site = yaml.safe_load(fread(CONFIG_FILE))    
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    env.filters["markdown"]= f_markdown
    env.globals["now"] = g_now
    
    pages = []
    for root,_,files in os.walk(CONTENT_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            pages.append(fm_load(filepath))

    for page in pages:
        t = env.get_template(page.get("template", BASE_TEMPLATE))
        html = t.render(site=site, pages=pages, page=page)
        path = os.path.join(PUBLIC_DIR, page.get("url", "index.html"))

        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        fwrite(path, html)
        print(f"{path}")

    generate_index_pages_for_directory(STATIC_DIR)

main()
