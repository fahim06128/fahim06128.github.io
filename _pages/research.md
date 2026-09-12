---
layout: page
permalink: /research/
title: Research
nav: true
nav_order: 2
---

<link rel="stylesheet" href="{{ '/assets/css/theme.css' | relative_url }}">

<div class="research-showcase-container">
  {% for item in site.data.research %}
    <article class="research-card" id="{{ item.id }}">
      <div class="research-card-inner">
        
        <!-- Left Column: Image / Gallery -->
        <div class="research-media-col">
          <div class="research-gallery" id="gallery-{{ item.id }}" data-total-slides="{{ item.images.size }}">
            <div class="gallery-track">
              {% for img in item.images %}
                <div class="gallery-slide {% if forloop.first %}active{% endif %}">
                  <div class="gallery-img-wrapper">
                    <img src="{{ img.src | relative_url }}" alt="{{ img.alt }}" class="gallery-img" loading="lazy">
                  </div>
                  {% if img.caption %}
                    <div class="gallery-caption">{{ img.caption }}</div>
                  {% endif %}
                </div>
              {% endfor %}
            </div>

            {% if item.images.size > 1 %}
              <!-- Navigation Controls -->
              <div class="gallery-controls">
                <button type="button" class="gallery-btn prev" aria-label="Previous image" onclick="moveSlide('gallery-{{ item.id }}', -1)">
                  <i class="fa-solid fa-chevron-left"></i>
                </button>
                <div class="gallery-indicators">
                  {% for img in item.images %}
                    <button type="button" class="gallery-dot {% if forloop.first %}active{% endif %}" aria-label="Slide {{ forloop.index }}" onclick="goToSlide('gallery-{{ item.id }}', {{ forloop.index0 }})"></button>
                  {% endfor %}
                </div>
                <button type="button" class="gallery-btn next" aria-label="Next image" onclick="moveSlide('gallery-{{ item.id }}', 1)">
                  <i class="fa-solid fa-chevron-right"></i>
                </button>
              </div>
            {% endif %}
          </div>
        </div>

        <!-- Right Column: Content -->
        <div class="research-content-col">
          <div class="research-type-tag">{{ item.type_label }}</div>
          <h2 class="research-card-title">{{ item.title }}</h2>
          
          <div class="research-card-meta">
            <div><strong>{{ item.institution }}</strong> &bull; {{ item.period }}</div>
            {% if item.supervisor and item.supervisor != "" %}
              <div class="meta-supervisor">Supervisor: <strong>{{ item.supervisor }}</strong></div>
            {% endif %}
          </div>

          <p class="research-summary-para">{{ item.summary }}</p>

          <ul class="research-bullets-list">
            {% for bullet in item.bullets %}
              <li>{{ bullet }}</li>
            {% endfor %}
          </ul>

          <div class="research-action-row">
            <a href="{{ item.brief_pdf | relative_url }}" target="_blank" rel="noopener noreferrer" class="research-brief-btn">
              <i class="fa-regular fa-file-pdf mr-1"></i> {{ item.action_label }}
            </a>
          </div>
        </div>

      </div>
    </article>
  {% endfor %}
</div>

<script>
function moveSlide(galleryId, direction) {
  const gallery = document.getElementById(galleryId);
  if (!gallery) return;
  const slides = gallery.querySelectorAll('.gallery-slide');
  if (slides.length <= 1) return;
  
  let activeIndex = 0;
  slides.forEach((s, idx) => {
    if (s.classList.contains('active')) activeIndex = idx;
  });
  
  let newIndex = (activeIndex + direction + slides.length) % slides.length;
  goToSlide(galleryId, newIndex);
}

function goToSlide(galleryId, targetIndex) {
  const gallery = document.getElementById(galleryId);
  if (!gallery) return;
  const slides = gallery.querySelectorAll('.gallery-slide');
  const dots = gallery.querySelectorAll('.gallery-dot');
  
  slides.forEach((s, idx) => {
    s.classList.toggle('active', idx === targetIndex);
  });
  dots.forEach((d, idx) => {
    d.classList.toggle('active', idx === targetIndex);
  });
}
</script>
