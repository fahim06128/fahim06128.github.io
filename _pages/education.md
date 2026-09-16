---
layout: page
permalink: /education/
title: Education
description: Academic background, degrees, relevant coursework, and professional certificates.
nav: true
nav_order: 1
---

<link rel="stylesheet" href="{{ '/assets/css/theme.css' | relative_url }}">

<div class="edu-page-container">

  <!-- ==========================================
       1. Academic Degrees & Institutions
       ========================================== -->
  <div class="edu-entry-list">
    {% for item in site.data.education %}
      <div class="edu-entry">
        {% if item.logo %}
          <div class="edu-logo-box">
            <img src="{{ item.logo | prepend: '/' | relative_url }}" alt="{{ item.short_name | default: item.institution }} Logo" class="edu-logo-img">
          </div>
        {% endif %}

        <div class="edu-details">
          <div class="edu-main-row">
            <h3 class="edu-degree-title">{{ item.degree }}</h3>
            {% if item.start_date and item.end_date %}
              <span class="edu-dates">{{ item.start_date }} &ndash; {{ item.end_date }}</span>
            {% endif %}
          </div>

          <div class="edu-inst-name">{{ item.institution }}</div>

          {% if item.department %}
            <div class="edu-dept">{{ item.department }}</div>
          {% endif %}

          {% if item.major %}
            <div class="edu-major-line">
              <span class="edu-major-label">Major: </span>
              <span class="edu-major-val">{{ item.major }}</span>
            </div>
          {% endif %}

          {% if item.cgpa or item.major_gpa or item.gpa or item.location %}
            <div class="edu-metrics-row">
              {% if item.location %}
                <span class="edu-metric-item"><i class="fa-solid fa-location-dot"></i> {{ item.location }}</span>
              {% endif %}
              {% if item.cgpa %}
                <span class="edu-metric-item">CGPA: <strong class="edu-metric-strong">{{ item.cgpa }}</strong></span>
              {% endif %}
              {% if item.major_gpa %}
                <span class="edu-metric-item">Major GPA: <strong class="edu-metric-strong">{{ item.major_gpa }}</strong></span>
              {% endif %}
              {% if item.gpa and item.cgpa == nil %}
                <span class="edu-metric-item">GPA: <strong class="edu-metric-strong">{{ item.gpa }}</strong></span>
              {% endif %}
            </div>
          {% endif %}

          {% if item.thesis %}
            <div class="edu-thesis-block">
              <span class="edu-thesis-label">Undergraduate Thesis:</span>
              <span class="edu-thesis-title">{{ item.thesis }}</span>
              {% if item.thesis_gpa %}
                <span class="edu-thesis-gpa">(GPA: <strong class="edu-metric-strong">{{ item.thesis_gpa }}</strong>)</span>
              {% endif %}
            </div>
          {% endif %}
        </div>
      </div>
    {% endfor %}
  </div>

  <!-- ==========================================
       2. Relevant Coursework
       ========================================== -->
  <h2 class="edu-section-title">
    <i class="fa-solid fa-book-open mr-2"></i> Relevant Coursework
  </h2>

  <div class="coursework-grid">
    {% for cat in site.data.coursework %}
      <div class="course-category-card">
        <h3 class="course-cat-title">{{ cat.category }}</h3>
        <ul class="course-bullets">
          {% for course in cat.courses %}
            <li>{{ course }}</li>
          {% endfor %}
        </ul>
      </div>
    {% endfor %}
  </div>

  <!-- ==========================================
       3. Certificates
       ========================================== -->
  <h2 class="edu-section-title">
    <i class="fa-solid fa-certificate mr-2"></i> Certificates
  </h2>

  <div class="cert-entry-list">
    {% for cert in site.data.certificates %}
      <div class="cert-entry-card">
        <div class="cert-icon-wrapper">
          <i class="fa-solid fa-award"></i>
        </div>

        <div class="cert-content">
          <div class="cert-header">
            <h3 class="cert-course-title">{{ cert.title }}</h3>
            {% if cert.date %}
              <span class="cert-date">{{ cert.date }}</span>
            {% endif %}
          </div>

          <div class="cert-issuer-line">
            <span class="cert-issuer-name">{{ cert.issuer }}</span>
            {% if cert.platform %}
              <span> · {{ cert.platform }}</span>
            {% endif %}
            {% if cert.instructor %}
              <span> · Instructor: {{ cert.instructor }}</span>
            {% endif %}
          </div>

          {% if cert.description %}
            <div class="cert-description">{{ cert.description }}</div>
          {% endif %}

          <div class="cert-links-row">
            {% if cert.pdf %}
              <a href="{{ cert.pdf | prepend: '/' | relative_url }}" class="cert-action-btn cert-btn-primary" target="_blank" rel="noopener noreferrer">
                <i class="fa-solid fa-file-pdf"></i> View Certificate <i class="fa-solid fa-arrow-up-right-from-square ml-1" style="font-size: 0.75rem;"></i>
              </a>
            {% endif %}
            {% if cert.credential_url %}
              <a href="{{ cert.credential_url }}" class="cert-action-btn cert-btn-secondary" target="_blank" rel="noopener noreferrer">
                <i class="fa-solid fa-shield-halved"></i> Verify Credential <i class="fa-solid fa-arrow-up-right-from-square ml-1" style="font-size: 0.75rem;"></i>
              </a>
            {% endif %}
            {% if cert.credential_id %}
              <span class="small text-muted ml-auto">Credential ID: <code>{{ cert.credential_id }}</code></span>
            {% endif %}
          </div>
        </div>
      </div>
    {% endfor %}
  </div>

</div>
