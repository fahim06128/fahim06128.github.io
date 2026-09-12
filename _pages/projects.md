---
layout: page
title: Projects
permalink: /projects/
description: Research, robotics, deep learning, and hardware systems projects.
nav: true
nav_order: 3
display_categories: ["Robotics & Vision", "Deep Learning & Vision", "Embedded Systems & IoT", "Digital Systems & Hardware"]
---

<link rel="stylesheet" href="{{ '/assets/css/theme.css' | relative_url }}">

<div class="project-showcase-container">
  {% for category in page.display_categories %}
    {% assign category_projects = site.data.projects | where: "category", category | sort: "importance" %}
    {% if category_projects.size > 0 %}
      <section class="project-category-section" id="{{ category | slugify }}">
        <div class="project-category-header">
          <h2 class="project-category-title">
            <i class="fa-solid fa-layer-group"></i> {{ category }}
          </h2>
          <span class="project-category-badge">{{ category_projects.size }} {% if category_projects.size == 1 %}Project{% else %}Projects{% endif %}</span>
        </div>

        <div class="project-category-cards">
          {% for project in category_projects %}
            <article class="project-card" id="{{ project.id }}">
              <div class="project-card-inner">
                
                <!-- Left Column: Photo Auto-Slide Carousel -->
                <div class="project-media-col" id="media-{{ project.id }}" onmouseenter="pauseProjectCycle('{{ project.id }}')" onmouseleave="resumeProjectCycle('{{ project.id }}')">
                  <div class="project-gallery" id="gallery-{{ project.id }}" data-total="{{ project.images.size }}">
                    <div class="project-slides-wrapper">
                      {% for img in project.images %}
                        <div class="project-slide {% if forloop.first %}active{% endif %}" data-index="{{ forloop.index0 }}">
                          <img src="{{ img.src | relative_url }}" alt="{{ img.alt }}" class="project-slide-img" loading="lazy">
                        </div>
                      {% endfor %}
                    </div>

                    {% if project.images.size > 1 %}
                      <!-- Bottom-Left Dash Indicators -->
                      <div class="project-dash-group" aria-label="Photo preview dashes">
                        {% for img in project.images %}
                          <button type="button" 
                                  class="project-dash {% if forloop.first %}active{% endif %}" 
                                  aria-label="View photo {{ forloop.index }}" 
                                  onclick="selectProjectSlide('{{ project.id }}', {{ forloop.index0 }})"
                                  onmouseenter="selectProjectSlide('{{ project.id }}', {{ forloop.index0 }})">
                          </button>
                        {% endfor %}
                      </div>

                      <!-- Subtle Arrow Navigation -->
                      <button type="button" class="project-gallery-nav prev" aria-label="Previous photo" onclick="stepProjectSlide('{{ project.id }}', -1)">
                        <i class="fa-solid fa-chevron-left"></i>
                      </button>
                      <button type="button" class="project-gallery-nav next" aria-label="Next photo" onclick="stepProjectSlide('{{ project.id }}', 1)">
                        <i class="fa-solid fa-chevron-right"></i>
                      </button>
                    {% endif %}

                    {% if project.images[0].caption %}
                      <div class="project-caption-tag" id="caption-{{ project.id }}">{{ project.images[0].caption }}</div>
                    {% endif %}
                  </div>
                </div>

                <!-- Right Column: Project Details -->
                <div class="project-content-col">
                  <div class="project-header-group">
                    <!-- Title First -->
                    <h3 class="project-title">{{ project.title }}</h3>
                    
                    <!-- Presentable Skills Badges -->
                    <div class="project-skills-wrapper">
                      {% if project.skills_list %}
                        {% for s in project.skills_list %}
                          <span class="project-skill-pill">{{ s }}</span>
                        {% endfor %}
                      {% elsif project.skills %}
                        {% assign raw_skills = project.skills | split: "•" %}
                        {% for s in raw_skills %}
                          <span class="project-skill-pill">{{ s | strip }}</span>
                        {% endfor %}
                      {% endif %}
                    </div>
                  </div>

                  <!-- Small Description Only (No Bullet Points) -->
                  <p class="project-desc">{{ project.description }}</p>

                  <!-- Action Buttons Row -->
                  <div class="project-btn-group">
                    {% if project.buttons.report %}
                      <a href="{{ project.buttons.report | relative_url }}" target="_blank" rel="noopener noreferrer" class="project-btn">
                        <i class="fa-regular fa-file-pdf"></i> Report
                      </a>
                    {% endif %}

                    {% if project.buttons.ppt %}
                      <a href="{{ project.buttons.ppt | relative_url }}" target="_blank" rel="noopener noreferrer" class="project-btn" download>
                        <i class="fa-regular fa-file-powerpoint"></i> PPT
                      </a>
                    {% endif %}

                    {% if project.buttons.demo %}
                      {% if project.buttons.demo_type == "video" %}
                        <button type="button" class="project-btn" onclick="openVideoPopup('{{ project.buttons.demo | relative_url }}', '{{ project.title | escape }}')">
                          <i class="fa-solid fa-play"></i> Demo
                        </button>
                      {% elsif project.buttons.demo_type == "youtube" %}
                        <a href="{{ project.buttons.demo }}" target="_blank" rel="noopener noreferrer" class="project-btn">
                          <i class="fa-brands fa-youtube"></i> Demo
                        </a>
                      {% else %}
                        <a href="{{ project.buttons.demo | relative_url }}" target="_blank" rel="noopener noreferrer" class="project-btn">
                          <i class="fa-solid fa-play"></i> Demo
                        </a>
                      {% endif %}
                    {% endif %}

                    {% if project.buttons.github %}
                      <a href="{{ project.buttons.github }}" target="_blank" rel="noopener noreferrer" class="project-btn">
                        <i class="fa-brands fa-github"></i> GitHub
                      </a>
                    {% endif %}
                  </div>
                </div>

              </div>
            </article>
          {% endfor %}
        </div>
      </section>
    {% endif %}
  {% endfor %}
</div>

<!-- Video Lightbox Popup -->
<div class="video-popup-overlay" id="videoPopup" onclick="handlePopupBackdropClick(event)">
  <div class="video-popup-container">
    <div class="video-popup-top">
      <div class="video-popup-title-group">
        <h4 class="video-popup-title" id="videoPopupTitle">Project Demo</h4>
      </div>
      <div class="video-popup-actions">
        <a id="popupVideoDirectLink" href="#" target="_blank" rel="noopener noreferrer" class="project-btn video-popup-ext-btn">
          <i class="fa-solid fa-arrow-up-right-from-square"></i> Open in tab
        </a>
        <button type="button" class="video-popup-close" onclick="closeVideoPopup()" aria-label="Close dialog">&times;</button>
      </div>
    </div>
    <div class="video-popup-content">
      <video id="popupVideoPlayer" controls playsinline preload="metadata">
        Your browser does not support HTML5 video.
      </video>
    </div>
  </div>
</div>

<script>
// Project Photo Auto-Slide Carousel Controller
const projectTimers = {};
const projectCaptions = {
  {% for p in site.data.projects %}
    "{{ p.id }}": [
      {% for img in p.images %}
        "{{ img.caption | escape }}"{% unless forloop.last %},{% endunless %}
      {% endfor %}
    ]{% unless forloop.last %},{% endunless %}
  {% endfor %}
};

function selectProjectSlide(projectId, index) {
  const gallery = document.getElementById('gallery-' + projectId);
  if (!gallery) return;

  const slides = gallery.querySelectorAll('.project-slide');
  const dashes = gallery.querySelectorAll('.project-dash');
  const captionTag = document.getElementById('caption-' + projectId);

  slides.forEach((s, idx) => {
    s.classList.toggle('active', idx === index);
  });
  dashes.forEach((d, idx) => {
    d.classList.toggle('active', idx === index);
  });

  if (captionTag && projectCaptions[projectId] && projectCaptions[projectId][index]) {
    captionTag.textContent = projectCaptions[projectId][index];
  }
}

function stepProjectSlide(projectId, delta) {
  const gallery = document.getElementById('gallery-' + projectId);
  if (!gallery) return;

  const slides = gallery.querySelectorAll('.project-slide');
  if (slides.length <= 1) return;

  let currentIdx = 0;
  slides.forEach((s, idx) => {
    if (s.classList.contains('active')) currentIdx = idx;
  });

  const nextIdx = (currentIdx + delta + slides.length) % slides.length;
  selectProjectSlide(projectId, nextIdx);
}

function startSlider(projectId, delay) {
  if (projectTimers[projectId]) clearInterval(projectTimers[projectId]);
  projectTimers[projectId] = setInterval(() => {
    stepProjectSlide(projectId, 1);
  }, delay || 2800);
}

function pauseProjectCycle(projectId) {
  if (projectTimers[projectId]) {
    clearInterval(projectTimers[projectId]);
    projectTimers[projectId] = null;
  }
}

function resumeProjectCycle(projectId) {
  startSlider(projectId, 2800);
}

function initProjectAutoSliders() {
  const galleries = document.querySelectorAll('.project-gallery');
  galleries.forEach((gallery, index) => {
    const total = parseInt(gallery.getAttribute('data-total') || '1', 10);
    if (total <= 1) return;
    const projectId = gallery.id.replace('gallery-', '');
    // Slightly stagger transitions so multiple cards cycle gracefully
    const delay = 2600 + (index % 4) * 350;
    startSlider(projectId, delay);
  });
}

// Auto-start slideshow immediately on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initProjectAutoSliders);
} else {
  initProjectAutoSliders();
}

// Video Popup Handlers
function openVideoPopup(videoSrc, title) {
  const popup = document.getElementById('videoPopup');
  const player = document.getElementById('popupVideoPlayer');
  const titleEl = document.getElementById('videoPopupTitle');
  const directLink = document.getElementById('popupVideoDirectLink');

  if (!popup || !player) return;

  titleEl.textContent = title || 'Project Demo';
  if (directLink) directLink.href = videoSrc;

  player.pause();
  player.src = videoSrc;
  player.load();

  popup.classList.add('active');
  player.play().catch(function() {});
}

function closeVideoPopup() {
  const popup = document.getElementById('videoPopup');
  const player = document.getElementById('popupVideoPlayer');

  if (!popup || !player) return;

  player.pause();
  player.removeAttribute('src');
  player.load();
  popup.classList.remove('active');
}

function handlePopupBackdropClick(event) {
  if (event.target && event.target.id === 'videoPopup') {
    closeVideoPopup();
  }
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeVideoPopup();
  }
});
</script>
