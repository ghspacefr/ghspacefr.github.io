---
title: Blog
---

{% set blog_posts = pages["blog"] | sort(attribute='last_update', reverse=True) %}

{% for item in blog_posts %}
- {{ item.last_update }}  [{{ item.title }}]({{ item.subpath }}){% endfor %}
