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
        
        <!-- Left Column: Content (Small Description Only, No Bullets) -->
        <div class="research-content-col">
          <div class="research-header-group">
            <div class="research-type-tag">{{ item.type_label }}</div>
            <h2 class="research-card-title">{{ item.title }}</h2>
            
            <div class="research-card-meta">
              <div><strong>{{ item.institution }}</strong> &bull; {{ item.period }}</div>
              {% if item.supervisor and item.supervisor != "" %}
                <div class="meta-supervisor">Supervisor: <strong>{{ item.supervisor }}</strong></div>
              {% endif %}
              {% if item.gpa and item.gpa != "" %}
                <div class="meta-gpa">Thesis GPA: <strong>{{ item.gpa }}</strong></div>
              {% endif %}
            </div>
          </div>

          <!-- Small Description Only (No Bullet Points) -->
          <p class="research-desc">{{ item.summary }}</p>

          <!-- Action Row -->
          <div class="research-btn-group">
            <a href="{{ item.brief_pdf | relative_url }}" target="_blank" rel="noopener noreferrer" class="research-brief-btn">
              <i class="fa-regular fa-file-pdf mr-1"></i> {{ item.action_label }}
            </a>
          </div>
        </div>

        <!-- Right Column: Auto-Slide Photo Carousel -->
        <div class="research-media-col" id="media-{{ item.id }}" onmouseenter="pauseResearchCycle('{{ item.id }}')" onmouseleave="resumeResearchCycle('{{ item.id }}')">
          <div class="research-gallery" id="gallery-{{ item.id }}" data-total="{{ item.images.size }}">
            <div class="research-slides-wrapper">
              {% for img in item.images %}
                <div class="research-slide {% if forloop.first %}active{% endif %}" data-index="{{ forloop.index0 }}">
                  <img src="{{ img.src | relative_url }}" alt="{{ img.alt }}" class="research-slide-img" loading="lazy">
                </div>
              {% endfor %}
            </div>

            {% if item.images.size > 1 %}
              <!-- Bottom Dash Indicators -->
              <div class="research-dash-group" aria-label="Photo preview dashes">
                {% for img in item.images %}
                  <button type="button" 
                          class="research-dash {% if forloop.first %}active{% endif %}" 
                          aria-label="View photo {{ forloop.index }}" 
                          onclick="selectResearchSlide('{{ item.id }}', {{ forloop.index0 }})"
                          onmouseenter="selectResearchSlide('{{ item.id }}', {{ forloop.index0 }})">
                  </button>
                {% endfor %}
              </div>

              <!-- Navigation Arrows -->
              <button type="button" class="research-gallery-nav prev" aria-label="Previous photo" onclick="stepResearchSlide('{{ item.id }}', -1)">
                <i class="fa-solid fa-chevron-left"></i>
              </button>
              <button type="button" class="research-gallery-nav next" aria-label="Next photo" onclick="stepResearchSlide('{{ item.id }}', 1)">
                <i class="fa-solid fa-chevron-right"></i>
              </button>
            {% endif %}

            {% if item.images[0].caption %}
              <div class="research-caption-tag" id="caption-{{ item.id }}">{{ item.images[0].caption }}</div>
            {% endif %}
          </div>
        </div>

      </div>
    </article>
  {% endfor %}
</div>

<script>
// Research Photo Auto-Slide Carousel Controller
const researchTimers = {};
const researchCaptions = {
  {% for r in site.data.research %}
    "{{ r.id }}": [
      {% for img in r.images %}
        "{{ img.caption | escape }}"{% unless forloop.last %},{% endunless %}
      {% endfor %}
    ]{% unless forloop.last %},{% endunless %}
  {% endfor %}
};

function selectResearchSlide(researchId, index) {
  const gallery = document.getElementById('gallery-' + researchId);
  if (!gallery) return;

  const slides = gallery.querySelectorAll('.research-slide');
  const dashes = gallery.querySelectorAll('.research-dash');
  const captionTag = document.getElementById('caption-' + researchId);

  slides.forEach((s, idx) => {
    s.classList.toggle('active', idx === index);
  });
  dashes.forEach((d, idx) => {
    d.classList.toggle('active', idx === index);
  });

  if (captionTag && researchCaptions[researchId] && researchCaptions[researchId][index]) {
    captionTag.textContent = researchCaptions[researchId][index];
  }
}

function stepResearchSlide(researchId, delta) {
  const gallery = document.getElementById('gallery-' + researchId);
  if (!gallery) return;

  const slides = gallery.querySelectorAll('.research-slide');
  if (slides.length <= 1) return;

  let currentIdx = 0;
  slides.forEach((s, idx) => {
    if (s.classList.contains('active')) currentIdx = idx;
  });

  const nextIdx = (currentIdx + delta + slides.length) % slides.length;
  selectResearchSlide(researchId, nextIdx);
}

function startResearchSlider(researchId, delay) {
  if (researchTimers[researchId]) clearInterval(researchTimers[researchId]);
  researchTimers[researchId] = setInterval(() => {
    stepResearchSlide(researchId, 1);
  }, delay || 2800);
}

function pauseResearchCycle(researchId) {
  if (researchTimers[researchId]) {
    clearInterval(researchTimers[researchId]);
    researchTimers[researchId] = null;
  }
}

function resumeResearchCycle(researchId) {
  startResearchSlider(researchId, 2800);
}

function initResearchAutoSliders() {
  const galleries = document.querySelectorAll('.research-gallery');
  galleries.forEach((gallery, index) => {
    const total = parseInt(gallery.getAttribute('data-total') || '1', 10);
    if (total <= 1) return;
    const researchId = gallery.id.replace('gallery-', '');
    // Slightly stagger transitions so multiple cards cycle gracefully
    const delay = 2600 + (index % 4) * 400;
    startResearchSlider(researchId, delay);
  });
}

// Auto-start slideshow immediately on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initResearchAutoSliders);
} else {
  initResearchAutoSliders();
}
</script>
