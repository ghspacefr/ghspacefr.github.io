---
title: Zine
---

{% set path = os.path.dirname(page.subpath) %}
{% for item in pages.keys() if item.startswith(path) and item != path %}
- [{{ os.path.relpath(item, path) }}]({{ os.path.join("/", item) }}){% endfor %}

[<< Retour](..)
