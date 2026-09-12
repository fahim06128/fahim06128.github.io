---
layout: page
permalink: /publications/
title: Publications
description: Peer-reviewed conference proceedings and research articles.
nav: true
nav_order: 4
---

<link rel="stylesheet" href="{{ '/assets/css/theme.css' | relative_url }}">

<!-- _pages/publications.md -->

<div class="publications">

{% bibliography %}

</div>

<!-- Publication Auto-Swiping Image Gallery Controller -->
<script>
(function() {
  const pubSlidesConfig = {
    "zakaria2026vision": [
      {
        src: "{{ '/assets/img/publications/icecte/path_replanning_arena.png' | relative_url }}",
        alt: "Real-Time Obstacle Avoidance & Path Replanning Arena",
        caption: "Path Replanning Arena"
      },
      {
        src: "{{ '/assets/img/publications/icecte/trajectory_tracking_pid.png' | relative_url }}",
        alt: "Trajectory Tracking vs Planned Path with PID Control",
        caption: "Trajectory Tracking & PID"
      },
      {
        src: "{{ '/assets/img/publications/icecte/segmentation_loss_curve.png' | relative_url }}",
        alt: "YOLOv11-seg Training vs Validation Segmentation Loss",
        caption: "Segmentation Loss Curves"
      }
    ]
  };

  const pubTimers = {};

  function initPubGalleries() {
    Object.keys(pubSlidesConfig).forEach(function(pubKey) {
      const pubEntry = document.getElementById(pubKey);
      if (!pubEntry) return;

      // Find the abbr column belonging to this publication entry
      const abbrCol = pubEntry.previousElementSibling;
      if (!abbrCol || !abbrCol.classList.contains('abbr')) return;

      // Avoid duplicate mount
      if (abbrCol.querySelector('.pub-gallery-box')) return;

      const slides = pubSlidesConfig[pubKey];
      if (!slides || slides.length === 0) return;

      // Build gallery DOM
      const container = document.createElement('div');
      container.className = 'pub-gallery-box';
      container.id = 'pubGallery-' + pubKey;

      let slidesHtml = '<div class="pub-slides-wrapper">';
      slides.forEach(function(s, idx) {
        slidesHtml += '<div class="pub-slide ' + (idx === 0 ? 'active' : '') + '">' +
          '<img src="' + s.src + '" alt="' + s.alt + '" loading="lazy">' +
          '</div>';
      });

      if (slides.length > 1) {
        slidesHtml += '<div class="pub-dash-group">';
        slides.forEach(function(_, idx) {
          slidesHtml += '<span class="pub-dash ' + (idx === 0 ? 'active' : '') + '" data-idx="' + idx + '"></span>';
        });
        slidesHtml += '</div>';
      }
      slidesHtml += '</div>';

      slidesHtml += '<div class="pub-caption-tag" id="pubCaption-' + pubKey + '">' + (slides[0].caption || '') + '</div>';
      container.innerHTML = slidesHtml;

      // Attach dash click events
      const dashes = container.querySelectorAll('.pub-dash');
      dashes.forEach(function(dash) {
        dash.addEventListener('click', function(e) {
          e.stopPropagation();
          const targetIdx = parseInt(dash.getAttribute('data-idx'), 10);
          selectPubSlide(pubKey, targetIdx);
        });
      });

      // Hover pause / resume
      container.addEventListener('mouseenter', function() {
        if (pubTimers[pubKey]) {
          clearInterval(pubTimers[pubKey]);
          pubTimers[pubKey] = null;
        }
      });
      container.addEventListener('mouseleave', function() {
        startPubTimer(pubKey);
      });

      // Append directly under <abbr> in the abbr column
      abbrCol.appendChild(container);

      // Start automatic swiping
      startPubTimer(pubKey);
    });
  }

  function selectPubSlide(pubKey, index) {
    const container = document.getElementById('pubGallery-' + pubKey);
    if (!container) return;

    const slides = container.querySelectorAll('.pub-slide');
    const dashes = container.querySelectorAll('.pub-dash');
    const captionEl = document.getElementById('pubCaption-' + pubKey);
    const config = pubSlidesConfig[pubKey];

    slides.forEach(function(s, idx) {
      s.classList.toggle('active', idx === index);
    });
    dashes.forEach(function(d, idx) {
      d.classList.toggle('active', idx === index);
    });

    if (captionEl && config && config[index]) {
      captionEl.textContent = config[index].caption || '';
    }
  }

  function stepPubSlide(pubKey) {
    const container = document.getElementById('pubGallery-' + pubKey);
    if (!container) return;

    const slides = container.querySelectorAll('.pub-slide');
    if (slides.length <= 1) return;

    let currentIdx = 0;
    slides.forEach(function(s, idx) {
      if (s.classList.contains('active')) currentIdx = idx;
    });

    const nextIdx = (currentIdx + 1) % slides.length;
    selectPubSlide(pubKey, nextIdx);
  }

  function startPubTimer(pubKey) {
    if (pubTimers[pubKey]) clearInterval(pubTimers[pubKey]);
    pubTimers[pubKey] = setInterval(function() {
      stepPubSlide(pubKey);
    }, 2800);
  }

  // Initialize immediately or on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPubGalleries);
  } else {
    initPubGalleries();
  }
})();
</script>

