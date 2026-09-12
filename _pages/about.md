---
layout: about
title: About Me
permalink: /
subtitle: BSc in Electrical & Electronic Engineering &middot; Communication & Signal Processing &middot; BUET

profile: false

selected_papers: false
social: false

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<link rel="stylesheet" href="{{ '/assets/css/theme.css' | relative_url }}">

<div class="profile float-right">
  <div class="profile-card">
    <img src="{{ site.data.profile.image | prepend: '/assets/img/' | relative_url }}" alt="{{ site.data.profile.name }}" class="profile-img-custom">
    <div class="profile-affiliation">
      <p>{{ site.data.profile.department }}</p>
      <p>{{ site.data.profile.institution }}</p>
      <p>{{ site.data.profile.location }}</p>
    </div>
    <div class="profile-social-compact">
      <div class="contact-icons">
        {% if site.data.socials.email %}
          <a href="mailto:{{ site.data.socials.email }}" title="Email"><i class="fa-solid fa-envelope"></i></a>
        {% endif %}
        {% if site.data.socials.scholar_userid %}
          <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}" title="Google Scholar" target="_blank" rel="noopener noreferrer"><i class="ai ai-google-scholar"></i></a>
        {% endif %}
        {% if site.data.socials.github_username %}
          <a href="https://github.com/{{ site.data.socials.github_username }}" title="GitHub" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-github"></i></a>
        {% endif %}
        {% if site.data.socials.whatsapp_url %}
          <a href="{{ site.data.socials.whatsapp_url }}" title="WhatsApp" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-whatsapp"></i></a>
        {% endif %}
      </div>
    </div>
  </div>
</div>

<p class="bio-paragraph">{{ site.data.profile.bio_p1 }}</p>

<p class="bio-paragraph">{{ site.data.profile.bio_p2 }}</p>

<div class="about-info-grid">
  <section class="about-info-block">
    <h2>Interests</h2>
    <ul class="interests-list">
      {% for interest in site.data.profile.interests %}
        <li>{{ interest }}</li>
      {% endfor %}
    </ul>
  </section>

  <section class="about-info-block">
    <h2>Education</h2>
    <div class="education-list">
      {% for item in site.data.education %}
        <div class="education-item">
          <div class="education-icon">
            <i class="fa-solid fa-graduation-cap"></i>
          </div>
          <div>
            <strong>{{ item.degree }}</strong>
            <span class="edu-inst">{{ item.institution }}</span>
            <span class="edu-meta">{{ item.start_date }} &ndash; {{ item.end_date }}</span>
          </div>
        </div>
      {% endfor %}
    </div>
  </section>
</div>
