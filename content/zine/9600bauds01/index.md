---
title: 9600bauds01
---

{% set path = os.path.dirname(page.subpath) %}

<a href="{{ os.path.join("/static/", path+".tar.gz")}}" class="right">
.tar.gz</a>

{% for item in pages.keys() if item.startswith(path) and item != path %}
- [{{ os.path.relpath(item, path) }}]({{ os.path.join("/", item) }}){% endfor %}
{% for item in pages[path] if item.subpath != page.subpath %}
- [{{ item.title }}]({{ os.path.join("/", item.subpath) }}){% endfor %}

[<< Retour](..)
