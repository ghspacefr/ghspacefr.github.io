import re
import os

import yaml

from datetime import datetime
from markdown import markdown

from jinja2 import Environment, FileSystemLoader
from rfeed import Item, Guid, Feed

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
            os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M'))
        fm_dict["content"] = content[match.end():] 
        fm_dict["url"] = os.path.normpath(
            os.path.relpath(path.replace(".md", ".html"), CONTENT_DIR))
     #   print(fm_dict)
        return fm_dict
    else:
        return {}

def f_markdown(data):
    return markdown(data, extensions=['attr_list', 'fenced_code'])

def g_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def gen_feed(pages, output_file="rss.xml"):

    items = []
    for page in pages:
        if not page["url"].startswith("blog"): continue
        items.append(Item(
            title = page["title"],
            link = f'{__site__["url"]}/{page["url"]}', 
            description = page["content"],
            author = "Unknown",
            guid = Guid(f'{__site__["url"]}/{page["url"]}'),
            pubDate = datetime.strptime(page["last_update"], "%Y-%m-%d %H:%M")
            ))

    feed = Feed(
        title = "GRENOBLE HACKERSPACE RSS Feed",
        link = os.path.join(__site__["url"], __site__["feed"]),
        description = "This is an example of how to use rfeed to generate an RSS 2.0 feed",
        language = "en-US",
        lastBuildDate = datetime.now(),
        items = items)

    fwrite(output_file, feed.rss())

def gen_index(dirpath, output_file='index.html'):
    # Get a list of all files and directories in the directory
    items = [ f for f in os.listdir(dirpath) if f != "index.html" ]
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en"><head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>Directory listing for {dirpath}</title>
    </head>
    <body>
    <h1>Directory listing for {dirpath}</h1>
    <hr>
    <ul>
    <li><a href="../">../</a></li>
    """

    for item in items: 
        href = os.path.join("/", dirpath, item)
        html += f'<li><a href="{href}">{item}</a></li>\n'

    html += "</ul>\n<hr>\n</body></html>"
    
    fwrite(output_file, html)
    print(f"Index page generated successfully: {output_file}")


def main():

    global __site__
    global __env__

    __site__ = yaml.safe_load(fread(CONFIG_FILE))
    __env__  = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    __env__.filters["markdown"]= f_markdown
    __env__.globals["now"] = g_now
    
    pages = []
    
    # Parse pages
    for root,_,files in os.walk(CONTENT_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            pages.append(fm_load(filepath))

    # Build pages
    for page in pages:
        t = __env__.get_template(page.get("template", BASE_TEMPLATE))
        html = t.render(site=__site__, pages=pages, page=page)
        path = os.path.join(PUBLIC_DIR, page.get("url", "index.html"))

        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        fwrite(path, html)
        print(f"Building page -> {path}")

    # Generate RSS Feed
    feed_path = os.path.join(PUBLIC_DIR, __site__["feed"])
    print(f"Building feed -> {feed_path}")
    gen_feed(pages, feed_path)

    # Generate IndexOf pages
    for root, dirs, files in os.walk(STATIC_DIR):
        _path = os.path.join(root, 'index.html')
        gen_index(root, _path)

main()
