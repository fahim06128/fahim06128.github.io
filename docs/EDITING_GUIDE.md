# Site Editing Guide

This guide explains how to edit and maintain your personal academic and research portfolio website.

---

## 1. Quick Reference: Where to Edit What

| Content Item                      | Source File                             | Description / Key Fields                                                         |
| :-------------------------------- | :-------------------------------------- | :------------------------------------------------------------------------------- |
| **Name & Professional Title**     | `_config.yml`                           | `first_name`, `last_name`, `title`                                               |
| **Academic Headline / Subtitle**  | `_data/profile.yml` & `_pages/about.md` | `headline`, `subtitle`                                                           |
| **Home Bio & Research Interests** | `_data/profile.yml`                     | `bio` (array of paragraphs), `interests` (ordered list)                          |
| **Profile Photo**                 | `assets/img/profile/photo1.jpg`         | Referenced in `_data/profile.yml` (`image`)                                      |
| **Social & Contact Links**        | `_data/socials.yml`                     | `email`, `scholar_userid`, `github_username`, `whatsapp_url`                     |
| **Theme / Color Palette**         | `assets/css/theme.css`                  | Dark navy palette variables (`--page-bg`, `--surface-bg`, etc.)                  |
| **Education Entries & Degrees**   | `_data/education.yml`                   | `institution`, `degree`, `major`, `cgpa`, `major_gpa`, `dates`, `thesis`, `logo` |
| **Relevant Coursework**           | `_data/coursework.yml`                  | `category`, `courses`                                                            |
| **Certificates**                  | `_data/certificates.yml`                | `title`, `issuer`, `date`, `credential_id`, `credential_url`, `pdf`              |
| **Research Experience**           | `_data/research_experience.yml`         | `title`, `role`, `institution`, `contributions`, `outcomes`                      |
| **Projects (Individual)**         | `_projects/<project_name>.md`           | Project frontmatter (`title`, `img`, `category`) and body                        |
| **Projects Landing Page**         | `_pages/projects.md`                    | Category tabs, display order                                                     |
| **Publications (BibTeX)**         | `_bibliography/papers.bib`              | BibTeX entries (`@inproceedings`, `@article`), `selected={true}`                 |
| **Author Highlighting**           | `_config.yml`                           | `scholar.last_name`, `scholar.first_name`                                        |
| **CV Data (Web View)**            | `_data/cv.yml`                          | Canonical RenderCV format (Education, Experience, Skills, etc.)                  |
| **CV PDF Download**               | `_pages/cv.md`                          | Uncomment `cv_pdf: /assets/pdf/<file>.pdf` after placing sanitized PDF           |
| **Navigation Order**              | `_pages/*.md`                           | `nav: true`, `nav_order: 1..6`                                                   |

---

## 2. Editing the Home / About Page

The homepage (`/`) is rendered by `_pages/about.md` following a clean academic reference layout (modeled after [mahinshahriar1.github.io](https://mahinshahriar1.github.io/)).

To keep the template clean and maintainable, **all editable homepage content lives in structured YAML files**:

### 1. Headline, Biography, and Research Interests (`_data/profile.yml`)

Edit `_data/profile.yml` to update your core academic narrative:

```yaml
name: "Md. Fahim"
headline: "BSc in Electrical & Electronic Engineering · BUET"
image: "profile/photo1.jpg"
department: "Department of EEE"
institution: "Bangladesh University of Engineering and Technology (BUET)"
location: "Dhaka, Bangladesh"

# Academic biography paragraphs (rendered sequentially on the homepage)
bio:
  - "I am a recent graduate in Electrical and Electronic Engineering from Bangladesh University of Engineering and Technology (BUET) majoring in communication and signal processing (CSP). My academic background has given me experience in signal processing, machine learning, embedded systems, and related areas of electrical engineering."
  - "My research interests include AI for healthcare, biomedical signal processing, robust and trustworthy clinical AI, signal processing, computer vision, edge AI and deployment, and robotics. I am particularly interested in developing reliable learning-based systems and translating algorithmic methods into practical applications."
  - "During my undergraduate studies, I worked on several research projects and developed a strong foundation in both theoretical concepts and practical implementations. I am passionate about solving complex engineering problems and contributing to cutting-edge research."

# Research Interests (rendered under 'Research Interests' with cyan triangle bullets ▹)
interests:
  - "AI for Healthcare"
  - "Biomedical Signal Processing"
  - "Robust & Trustworthy Clinical AI"
  - "Signal Processing"
  - "Computer Vision"
  - "Edge AI & Deployment"
  - "Robotics"
```

#### How to manage homepage content:

- **Editing Homepage Headline**: Change `headline:` in `_data/profile.yml` and `subtitle:` in `_pages/about.md` to update the concise title line underneath your name (e.g., `BSc in Electrical & Electronic Engineering · BUET`).
- **Editing Biography Paragraphs**: Modify or add items under `bio:` in `_data/profile.yml`. Each array element (`- "..."`) renders as its own paragraph `<p class="bio-paragraph">`.
- **Editing Research Interests**: Modify items under `interests:` in `_data/profile.yml`.
- **Reordering Research Interests**: Simply move lines up or down under `interests:`; the homepage renders them in the exact order specified in this YAML file.
- **Adding / Removing an Interest**: To add an interest, append `- "New Interest Name"`. To remove an interest, delete or comment out the line. The layout automatically updates and balances with the Education section.

### 2. Profile Photo (`assets/img/profile/photo1.jpg`)

- To update your portrait, place a new JPG image in `assets/img/profile/` and update `image:` in `_data/profile.yml`.
- The image is automatically styled via `assets/css/theme.css` with natural height scaling, a subtle `6px` border radius, and card shadow.

### 3. Contact & Social Links (`_data/socials.yml`)

Edit `_data/socials.yml` to update your icons beneath the profile photo:

```yaml
email: mdfahim.buet@gmail.com
scholar_userid: KKSUYLAAAAAJ
github_username: fahim06128
whatsapp_url: https://wa.me/8801957954950
```

_Privacy Note: The WhatsApp link directs users to chat via WhatsApp without exposing your raw phone number in visible page text._

---

## 3. Editing the Education Page

The Education page (`/education/`) is rendered by `_pages/education.md` using three structured data files. You can perform all routine edits without modifying HTML or Liquid templates.

### 1. Adding or Editing a Degree / Institution (`_data/education.yml`)

All degrees and academic qualifications are managed in `_data/education.yml`:

```yaml
- institution: "Bangladesh University of Engineering and Technology (BUET)"
  short_name: "BUET"
  logo: "assets/img/education/buet-logo.png"
  degree: "Bachelor of Science in Electrical and Electronic Engineering"
  department: "Department of Electrical and Electronic Engineering"
  major: "Communication and Signal Processing (CSP)"
  start_date: "Jan. 2022"
  end_date: "June 2026"
  location: "Dhaka, Bangladesh"
  cgpa: "3.44 / 4.00"
  major_gpa: "3.81 / 4.00"
  thesis: "Morphology-Aware ECG Denoising Using Deep Neural Networks for Arrhythmia Detection"
```

#### Changing Institution Logos

- **Asset directory**: `assets/img/education/`
- **Recommended format**: Transparent PNG or vector SVG
- **Recommended dimensions**: ~300×300 px (displayed at 64×64 px with automatic aspect ratio preservation)
- **Controlling field**: `logo: "assets/img/education/<filename>.png"` (relative to site root)

#### Changing GPA & CGPA

- **Overall CGPA**: Update `cgpa: "3.44 / 4.00"`
- **Major GPA**: Update `major_gpa: "3.81 / 4.00"`
- **General GPA (e.g. for high school)**: Update `gpa: "5.00 / 5.00"`

#### Changing Undergraduate Thesis Title

- Update `thesis: "Your New Thesis Title"` in the corresponding institution block.

#### Optional Fields

All fields are optional. If an entry does not have `department`, `major`, `major_gpa`, or `thesis` (such as high school), simply omit the line and it will not render an empty label.

---

### 2. Relevant Coursework (`_data/coursework.yml`)

Relevant courses are organized into academic and research-oriented categories in `_data/coursework.yml`.

#### Adding a Course

Add a new item under the appropriate category:

```yaml
- category: "Artificial Intelligence, Signal Processing & Biomedical"
  courses:
    - "Artificial Intelligence and Machine Learning"
    - "Digital Signal Processing I"
    - "Random Signals and Processes"
    - "Introduction to Medical Imaging"
    - "Deep Learning for Computer Vision" # <-- New course added here
```

#### Adding a New Category

Add a new category block at the desired position in `_data/coursework.yml`:

```yaml
- category: "Mathematics & Optimization"
  courses:
    - "Linear Algebra and Complex Variables"
    - "Probability and Statistics"
```

#### Moving a Course Between Categories

Simply cut the line `- "Course Name"` from one category's `courses` list and paste it under another category's `courses` list.

---

### 3. Certificates (`_data/certificates.yml`)

Certificates and verified professional credentials are listed in `_data/certificates.yml`.

#### Adding a New Certificate

Add a block to `_data/certificates.yml`:

```yaml
- title: "Supervised Machine Learning: Regression and Classification"
  issuer: "DeepLearning.AI & Stanford Online"
  platform: "Coursera"
  instructor: "Andrew Ng"
  date: "August 2024"
  credential_id: "JIIZ7UTR4THX"
  credential_url: "https://coursera.org/verify/JIIZ7UTR4THX"
  pdf: "assets/pdf/certificates/supervised-machine-learning-coursera.pdf"
  description: "Foundational machine learning covering linear regression, logistic regression, gradient descent, feature engineering, and regularization."
```

#### Replacing or Adding Certificate PDF Files

1. Save the sanitized public PDF in `assets/pdf/certificates/<certificate-slug>.pdf`.
2. Update the `pdf:` field in `_data/certificates.yml`:
   ```yaml
   pdf: "assets/pdf/certificates/<certificate-slug>.pdf"
   ```
3. Update `credential_url:` with the direct official verification link (e.g. `https://coursera.org/verify/...`).

---

## 4. Research Showcase (`/research/`)

The Research page functions as a concise showcase containing two horizontal cards:

1. **Undergraduate Thesis:** Morphology-Aware ECG Denoising Using Deep Neural Networks for Arrhythmia Detection
2. **Ongoing Research:** Weakly Supervised Temporal Action Localization for Non-Intrusive Load Monitoring

All content is decoupled into `_data/research.yml` and rendered dynamically by `_pages/research.md`.

### Editing Research Showcase Cards in `_data/research.yml`

- **Change Thesis Title:** Edit the `title` field under `id: thesis`.
- **Change Supervisor:** Edit the `supervisor` field under `id: thesis` (e.g. `supervisor: "Dr. Md. Kamrul Hasan"`).
- **Edit Three Bullets:** Modify the 3 list items under `bullets:` for either entry (`thesis` or `nilm-wtal`).
- **Edit Summary Paragraph:** Edit the `summary:` field (keep between 45–70 words for optimal visual balance).
- **Replace Thesis Carousel Image:**
  1. Add the new image to `assets/img/research/thesis/<image-name>.png`.
  2. Update the `src` path in the `images:` array in `_data/research.yml`.
- **Reorder Carousel Images:**
  Rearrange the order of dictionary entries inside the `images:` list in `_data/research.yml`. The first image in the list will be the active starting slide.
- **Add / Remove Carousel Image:**
  Add or remove `- src: "..." alt: "..." caption: "..."` entries under `images:`. The navigation dots and controls adjust dynamically.
- **Edit NILM Information:**
  Edit fields under `id: nilm-wtal` in `_data/research.yml` (`title`, `period`, `summary`, `bullets`, `images`, `brief_pdf`).

---

## 4.1. Editing Research Brief PDFs

Both research entries link to dedicated, concise **one-page academic research briefs** in PDF format via the `View Research Brief ↗` button.

### Editable Markdown Source Files

- **Thesis Research Brief Source:** `research-briefs/thesis-research-brief.md`
- **NILM Research Brief Source:** `research-briefs/nilm-wtal-research-brief.md`

### Source Traceability Comments

Inside the Markdown source files, hidden HTML comments document the exact page and section in source documents (e.g. `<!-- Source: Thesis Abstract, page 16 -->`). These comments are automatically stripped during PDF compilation and do not appear in the final documents.

### Regenerating PDFs

To compile the Markdown source files into 1-page PDFs, run:

```bash
python scripts/build_research_briefs.py
```

This script automatically detects your local Chrome or Edge browser in headless mode, applies academic typography styles with strict 1-page constraints, and validates that each output is exactly 1 page using `pypdf`.

### Output Locations

- `assets/pdf/research/thesis-research-brief.pdf`
- `assets/pdf/research/nilm-wtal-research-brief.pdf`

---

## 5. Projects (`/projects/`)

Each project has its own Markdown file inside the `_projects/` directory.

### Adding a New Project

Create `_projects/<number>_<project_slug>.md`:

```markdown
---
layout: page
title: Project Title
description: A 1-2 sentence summary of what this project does.
img: assets/img/<thumbnail>.jpg
importance: 1 # Lower numbers appear first
category: "Robotics & Vision" # Must match category in _pages/projects.md
github: https://github.com/fahim06128/<repo> # optional
---

### Overview

Detailed explanation of project background, objectives, and problem solved.

### Key Technical Contributions

- Contribution 1
- Contribution 2

### Tools & Technologies

- Python, PyTorch, ESP32, etc.
```

---

## 6. Publications (`/publications/`)

Publications are stored in `_bibliography/papers.bib` and rendered via `jekyll-scholar`.

### Adding a New Publication

Add a BibTeX entry in `_bibliography/papers.bib`:

```bibtex
@inproceedings{yourkey2026,
  abbr        = {VENUE_ACRONYM},
  bibtex_show = {true},
  title       = {Paper Title},
  author      = {Author, One and Fahim, Md. and Author, Three},
  booktitle   = {Conference or Journal Name},
  year        = {2026},
  doi         = {10.1109/XXXXX},
  url         = {https://doi.org/10.1109/XXXXX},
  html        = {https://doi.org/10.1109/XXXXX},
  pdf         = {paper_slug.pdf}, # place in assets/pdf/ if hosting local PDF
  selected    = {true}
}
```

_Your name (`Fahim, Md.`) is automatically highlighted because it matches `scholar.last_name` in `_config.yml`._

---

## 7. CV (Web Page & Downloadable PDF)

### Editing the Web CV

The canonical CV data file is `_data/cv.yml` (RenderCV format). Edit the sections:

- `sections.Education`
- `sections.Experience`
- `sections.Publications`
- `sections.Projects`
- `sections.Awards`
- `sections.Skills`
- `sections.References`

### Enabling the Downloadable PDF

1. Ensure your PDF has all private phone numbers and personal home addresses removed.
2. Place the PDF in `assets/pdf/CV_Md_Fahim.pdf`.
3. In `_pages/cv.md`, uncomment the `cv_pdf` line:
   ```yaml
   cv_pdf: /assets/pdf/CV_Md_Fahim.pdf
   ```
4. In `_data/socials.yml`, you can also uncomment `cv_pdf` to display the PDF icon next to your email/GitHub icons.

---

## 8. Top Navigation Order

The navigation bar displays pages in the following sequence:

1. **About Me**: Configured in `_pages/about.md` (`permalink: /`, `title: About Me`)
2. **Education**: `_pages/education.md` (`nav_order: 1`)
3. **Research Experience**: `_pages/research-experience.md` (`nav_order: 2`)
4. **Projects**: `_pages/projects.md` (`nav_order: 3`)
5. **Publications**: `_pages/publications.md` (`nav_order: 4`)
6. **CV**: `_pages/cv.md` (`nav_order: 5`)

To hide a page from the navbar, change `nav: true` to `nav: false`.

---

## 9. Previewing Locally

Run the following command from the repository root:

```bash
bundle exec jekyll serve
```

Then visit:

```
http://localhost:4000/al-folio/
```

_(Note: Always include the `/al-folio/` base path in the URL)._
