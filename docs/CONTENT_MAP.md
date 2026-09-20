# Content Map

This document maps every visible section and element on the website to its corresponding source file in the repository.

---

## 1. Global Components

| Visible Section / Element       | Source File(s)                                    | Notes                                                                                                                |
| :------------------------------ | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------- |
| **Site Name & Title in Navbar** | `_config.yml` (`first_name`, `last_name`)         | Appears top-left on non-home pages.                                                                                  |
| **Website Logo & Favicon**      | `assets/img/logo.png`, `_config.yml` (`icon`)     | Brand logo displayed in navbar brand on subpages and as browser tab favicon/bookmark.                                |
| **Top Navigation Links**        | `_pages/*.md` (`title`, `nav: true`, `nav_order`) | Sorted by `nav_order`: About Me (1), Education (2), Research Experience (3), Projects (4), Publications (5), CV (6). |
| **Dark Navy Academic Theme**    | `assets/css/theme.css`                            | Defines CSS custom properties (`--page-bg`, `--surface-bg`, etc.) and styles navbar, cards, and body.                |
| **Theme Toggle (Light/Dark)**   | `_config.yml` (`enable_darkmode`)                 | Handled automatically by `al_folio_core`.                                                                            |
| **Search Palette (`Ctrl + K`)** | `_config.yml` (`search_enabled`)                  | Handled by `al_search`.                                                                                              |
| **Footer Text**                 | `_config.yml` (`footer_text`, `last_updated`)     | Appears at the bottom of every page.                                                                                 |

---

## 2. About Me / Home Page (`/`)

The home landing page follows the streamlined visual structure of `mahinshahriar1.github.io`:

| Visible Section / Element        | Source File(s)                                                                     | Notes                                                                                                                              |
| :------------------------------- | :--------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **Page Title ("About Me")**      | `_pages/about.md` (`title`)                                                        | Displayed as post title / header.                                                                                                  |
| **Academic Headline / Subtitle** | `_pages/about.md` (`subtitle`) & `_data/profile.yml` (`headline`)                  | E.g. _"BSc in Electrical & Electronic Engineering · BUET"_.                                                                        |
| **Profile Photo**                | `assets/img/profile/photo1.jpg`, `_data/profile.yml` (`image`)                     | Crisp portrait with rounded corners and shadow.                                                                                    |
| **Affiliation Text**             | `_data/profile.yml` (`department`, `institution`, `location`)                      | Department of EEE, BUET, Dhaka, Bangladesh.                                                                                        |
| **Compact Social Icons**         | `_data/socials.yml` (`email`, `scholar_userid`, `github_username`, `whatsapp_url`) | Rendered compactly beneath the photo. WhatsApp icon points to `https://wa.me/8801957954950` with no raw phone number in text.      |
| **Academic Biography**           | `_data/profile.yml` (`bio`)                                                        | Exactly 3 concise academic paragraphs detailing background, research interests, and prospective graduate study.                    |
| **Two-Column Info Grid**         | `_pages/about.md`, `assets/css/theme.css`                                          | 2 balanced columns on desktop (Research Interests on left, Education on right); stacks to 1 column on mobile ($\le 768\text{px}$). |
| **Research Interests List**      | `_data/profile.yml` (`interests`)                                                  | 7 concise bulleted items with cyan triangle markers (`▹`).                                                                         |
| **Education Summary**            | `_data/education.yml`                                                              | Compact list showing degrees, institutions, and dates with graduation cap icons (`fa-graduation-cap`).                             |

---

## 3. Education Page (`/education/`)

The Education page follows the clean academic information hierarchy of `rifahnanzeeba.github.io/education.html` across three dedicated sections:

| Visible Section / Element          | Source File(s)                                                                                       | Notes                                                                                                     |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Page Header & Description**      | `_pages/education.md` (`title`, `description`)                                                       | "Academic background, degrees, relevant coursework, and professional certificates."                       |
| **BUET Degree**                    | `_data/education.yml` (`degree: "Bachelor of Science in Electrical and Electronic Engineering"`)     | Main degree title.                                                                                        |
| **BUET Dates**                     | `_data/education.yml` (`start_date`, `end_date`)                                                     | "Jan. 2022 – June 2026"                                                                                   |
| **BUET Department & Major**        | `_data/education.yml` (`department`, `major`)                                                        | Department of EEE; Major: Communication and Signal Processing (CSP).                                      |
| **BUET CGPA**                      | `_data/education.yml` (`cgpa: "3.44 / 4.00"`)                                                        | Overall cumulative grade point average.                                                                   |
| **BUET Major GPA**                 | `_data/education.yml` (`major_gpa: "3.81 / 4.00"`)                                                   | Specialization major grade point average.                                                                 |
| **BUET Thesis Title & GPA**        | `_data/education.yml` (`thesis`, `thesis_gpa`)                                                       | "Morphology-Aware ECG Denoising Using Deep Neural Networks for Arrhythmia Detection" (GPA: 4.00 / 4.00).  |
| **BUET Logo**                      | `assets/img/education/buet-logo.png`                                                                 | Official high-resolution transparent PNG logo.                                                            |
| **NDC Information (Degree & GPA)** | `_data/education.yml` (`degree`, `institution`, `major`, `start_date`, `end_date`, `gpa`)            | Higher Secondary Certificate (HSC), Science; GPA: 5.00 / 5.00.                                            |
| **NDC Logo**                       | `assets/img/education/ndc-logo.png`                                                                  | Official high-resolution transparent PNG monogram.                                                        |
| **Relevant Coursework**            | `_data/coursework.yml`                                                                               | 16 verified BUET EEE courses categorized into 4 research clusters.                                        |
| **Certificates Metadata**          | `_data/certificates.yml`                                                                             | Machine Learning credential (DeepLearning.AI & Stanford Online via Coursera, Aug 2024, ID: JIIZ7UTR4THX). |
| **Certificate Document**           | `assets/pdf/certificates/supervised-machine-learning-coursera.pdf`                                   | Sanitized public PDF linked directly with new-tab target.                                                 |
| **Education Page Styles**          | `assets/css/theme.css` (`.edu-page-container`, `.edu-entry`, `.coursework-grid`, `.cert-entry-card`) | Responsive styling for entries, 2-column coursework grid, and certificate cards.                          |

---

## 4. Research Page (`/research/`)

| Visible Content / Component      | Source File(s) & Path(s)                                                           | Notes                                                                                                                     |
| :------------------------------- | :--------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| **Page Template**                | `_pages/research.md` (`title: Research`, `permalink: /research/`)                  | Clean showcase page (nav_order: 2).                                                                                       |
| **Legacy URL Redirect**          | `_pages/research-experience.md` (`permalink: /research-experience/`)               | Auto-redirects `/research-experience/` to `/research/`.                                                                   |
| **Thesis Title**                 | `_data/research.yml` (`id: thesis` &bull; `title`)                                 | "Morphology-Aware ECG Denoising Using Deep Neural Networks for Arrhythmia Detection".                                     |
| **Thesis Supervisor**            | `_data/research.yml` (`id: thesis` &bull; `supervisor`)                            | "Dr. Md. Kamrul Hasan" (Professor, Dept. of EEE, BUET).                                                                   |
| **Thesis GPA**                   | `_data/research.yml` (`id: thesis` &bull; `gpa`)                                   | "4.00 / 4.00".                                                                                                            |
| **Thesis Summary**               | `_data/research.yml` (`id: thesis` &bull; `summary`)                               | Single concise paragraph (62 words, grounded in thesis Abstract).                                                         |
| **Thesis Bullets**               | `_data/research.yml` (`id: thesis` &bull; `bullets`)                               | Exactly three bullets answering research questions & validated outcomes.                                                  |
| **Thesis Carousel Images**       | `assets/img/research/thesis/` &bull; `_data/research.yml` (`images`)               | Clean non-architecture figures: `ecg-reconstruction-waveform.png`, `ecg-snr-performance.png`, `ecg-noise-robustness.png`. |
| **Thesis Research Brief Source** | `research-briefs/thesis-research-brief.md`                                         | Editable Markdown source with hidden section/page trace comments.                                                         |
| **Thesis Research Brief PDF**    | `assets/pdf/research/thesis-research-brief.pdf`                                    | Exactly 1-page academic PDF summary.                                                                                      |
| **NILM Title**                   | `_data/research.yml` (`id: nilm-wtal` &bull; `title`)                              | "Weakly Supervised Temporal Action Localization for Non-Intrusive Load Monitoring".                                       |
| **NILM Summary**                 | `_data/research.yml` (`id: nilm-wtal` &bull; `summary`)                            | Single concise ongoing-research paragraph (62 words).                                                                     |
| **NILM Bullets**                 | `_data/research.yml` (`id: nilm-wtal` &bull; `bullets`)                            | Exactly three bullets covering problem, weak supervision, and localization.                                               |
| **NILM Carousel Image**          | `assets/img/research/nilm-wtal/nilm_wtal_pipeline.svg` &bull; `_data/research.yml` | Custom conceptual pipeline vector SVG.                                                                                    |
| **NILM Research Brief Source**   | `research-briefs/nilm-wtal-research-brief.md`                                      | Editable Markdown source citing CamAL baseline with hidden comments.                                                      |
| **NILM Research Brief PDF**      | `assets/pdf/research/nilm-wtal-research-brief.pdf`                                 | Exactly 1-page academic PDF summary.                                                                                      |
| **Research Card & Gallery CSS**  | `assets/css/theme.css` (`.research-card`, `.research-media-col`, `.gallery-*`)     | Compact horizontal cards, responsive 46%/54% desktop split, mobile stack.                                                 |
| **PDF Generation Command**       | `python scripts/build_research_briefs.py`                                          | Reproducible script compiling both Markdown briefs to 1-page PDFs.                                                        |

---

## 5. Projects Page (`/projects/`)

| Visible Section / Element           | Source File(s)                                             | Notes                                               |
| :---------------------------------- | :--------------------------------------------------------- | :-------------------------------------------------- |
| **Page Header & Description**       | `_pages/projects.md` (`title`, `description`)              | Filtered by categories.                             |
| **Category Sections**               | `_pages/projects.md` (`display_categories`)                | "Robotics & Vision", "Deep Learning & Vision", etc. |
| **Individual Project Cards**        | `_projects/*.md` (`title`, `description`, `img`, `github`) | Displays thumbnail, brief summary, and GitHub link. |
| **Automated Transportation Robot**  | `_projects/1_automated_object_transportation.md`           | ESP32, ArUco, YOLOv11-seg, A\* algorithm.           |
| **HIVE-R Swarm Drone**              | `_projects/2_hive_r_swarm_drone.md`                        | Raspberry Pi 4, Pixhawk, Visual SLAM, YOLOv8 Nano.  |
| **Smart Prepaid Energy Meter**      | `_projects/3_smart_prepaid_energy_meter.md`                | Arduino, IoT wireless billing, relay cut-off.       |
| **Camera-to-Camera Style Transfer** | `_projects/4_camera_to_camera_style_transfer.md`           | PyTorch, StarGAN v2, IEEE SP Cup 2018.              |
| **Two-Player Pong on CPLD**         | `_projects/5_two_player_pong_cpld.md`                      | Verilog HDL, Quartus 7.1, FSMs, LED matrices.       |

---

## 6. Publications Page (`/publications/`)

| Visible Section / Element           | Source File(s)                                                   | Notes                                            |
| :---------------------------------- | :--------------------------------------------------------------- | :----------------------------------------------- |
| **Page Header & Search Box**        | `_pages/publications.md`                                         | Bibsearch feature for searching papers.          |
| **Publication Entry (ICECTE 2026)** | `_bibliography/papers.bib` (`@inproceedings{zakaria2026vision}`) | Verified conference paper entry.                 |
| **Author Highlighting**             | `_config.yml` (`scholar.last_name: [Fahim]`)                     | Automatically bolds "Fahim, Md." in author list. |
| **DOI & HTML Links**                | `_bibliography/papers.bib` (`doi`, `html`, `url`)                | Links directly to official IEEE publication.     |

---

## 7. CV Page (`/cv/`)

| Visible Section / Element     | Source File(s)                                        | Notes                                            |
| :---------------------------- | :---------------------------------------------------- | :----------------------------------------------- |
| **Page Header & Description** | `_pages/cv.md` (`title`, `description`)               | Displays web CV.                                 |
| **PDF Download Button**       | `_pages/cv.md` (`cv_pdf`)                             | Disabled until a public PDF is provided.         |
| **Contact Information Box**   | `_data/cv.yml` (`cv.name`, `cv.email`, `cv.location`) | Private numbers omitted.                         |
| **Professional Summary**      | `_data/cv.yml` (`cv.summary`)                         | High-level research summary.                     |
| **Experience Section**        | `_data/cv.yml` (`sections.Experience`)                | Thesis research and instructional experience.    |
| **Education Section**         | `_data/cv.yml` (`sections.Education`)                 | BUET and Notre Dame College.                     |
| **Publications Section**      | `_data/cv.yml` (`sections.Publications`)              | IEEE ICECTE 2026 paper.                          |
| **Projects Section**          | `_data/cv.yml` (`sections.Projects`)                  | 5 verified engineering & AI projects.            |
| **Awards Section**            | `_data/cv.yml` (`sections.Awards`)                    | EEE Day 2026, Robo Carnival, Astronomy Olympiad. |
