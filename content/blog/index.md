---
title: Blog
---

{% set blog_posts = pages["blog"] | sort(attribute='last_update', reverse=True) %}

{% for item in blog_posts if not item.subpath.endswith('index.html') %}
- {{ item.last_update }} [{{ item.title }}](/{{ item.subpath }}){% endfor %}
