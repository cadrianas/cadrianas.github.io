---
layout: page
title: Teaching
permalink: /teaching/
description: Material for some courses both current or recent and past.
nav: true
display_categories: ["University of Manitoba", "Others", "Older UM"]
horizontal: true
---

<!-- pages/teaching.md -->
<div class="projects">
{%- if site.enable_teaching_categories and page.display_categories %}
  <!-- Display categorized teaching -->
  {%- for category in page.display_categories %}
  {%- assign categorized_teaching = site.teaching | where: "category", category -%}
  {%- if categorized_teaching.size > 0 %}
  <h2 class="category">{{ category }}</h2>
  {%- assign sorted_teaching = categorized_teaching | sort: "importance" | default: "" %}
  <!-- Generate cards for each teaching -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_teaching -%}
      {% include projects_horizontal.liquid %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_teaching -%}
      {% include projects.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display teaching without categories -->
  {%- assign sorted_teaching = site.teaching | default: "" | sort: "importance" -%}
  <!-- Generate cards for each teaching -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_teaching -%}
      {% include projects_horizontal.liquid %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_teaching -%}
      {% include projects.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>