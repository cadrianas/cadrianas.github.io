---
layout: page
permalink: /repositories/
title: repositories
description: some of my open-source projects.
nav: true
nav_order: 4
---

{% if site.data.repositories.github_users %}
  <div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
    {% for user in site.data.repositories.github_users %}
      {% include repository/repo_user.liquid username=user %}
    {% endfor %}
  </div>
{% endif %}

{% if site.data.repositories.github_repos %}
  <div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
    {% for repo in site.data.repositories.github_repos %}
      {% assign repo_url = repo | remove: 'https://github.com/' %}
      {% include repository/repo.liquid repository=repo_url %}
    {% endfor %}
  </div>
{% endif %}
