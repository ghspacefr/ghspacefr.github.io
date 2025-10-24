---
title: eZine
---

{% set path = "static/zine" %}
<ul style="list-style-type: none;">
<b>Name</b> <b class="right">Size</b>
</ul>
{% for item in os.listdir(path) %}{% set subpath = os.path.join(path, item) %}
- [{{ item }}](/{{subpath}}) <span class="right">{{ os.path.getsize(subpath) | format_size }}<span>{% endfor %}
