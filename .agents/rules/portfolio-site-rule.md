# Portfolio Site Workspace Rule

This workspace is a personal academic/research website based on the current **al-folio** Jekyll template.

## Mission

Maintain a polished academic portfolio for PhD applications, research outreach, collaboration, and technical/research roles.

Primary navigation:

1. About Me
2. Education
3. Research Experience
4. Projects
5. Publications
6. CV

The About Me page is the home page.

## Non-negotiable content rules

- Never invent biographical, academic, publication, project, affiliation, award, metric, date, supervisor, venue, DOI, or URL information.
- User-provided CV/materials are the factual source of truth until superseded by later user instructions.
- Preserve official names and statuses.
- Distinguish ongoing, submitted, under review, accepted, and published work accurately.
- Do not expose private address, private phone number, IDs, or sensitive CV data by default.
- Do not leave demo al-folio content in public pages.
- Missing data should be represented by a documented TODO or an omitted optional field, never fabricated filler.

## al-folio architecture rule

This project may use al-folio v1.x, where the starter is intentionally thin and runtime behavior is plugin/gem-owned.

Before structural changes:

- inspect repository version/configuration;
- read repository `AGENTS.md` and relevant `docs/` guidance;
- respect plugin ownership boundaries;
- prefer site-owned Markdown, YAML, BibTeX, assets, collections, Sass tokens/overrides, configuration, and narrow local overrides;
- do not copy or rewrite gem-owned layouts/includes/runtime assets merely to make a small site customization;
- do not introduce a parallel frontend framework.

Use native al-folio content structures where practical:

- `_config.yml`
- `_data/socials.yml`
- canonical CV source (`_data/cv.yml` OR `assets/json/resume.json`)
- `_bibliography/papers.bib`
- `_projects/*.md`
- `_pages/*.md`
- `assets/img/`
- supported public PDF location

Custom Education and Research Experience content should remain easy to edit from site-owned data/content files without touching theme internals.

## Source-of-truth discipline

Avoid duplicated personal data.

If the same fact appears on multiple pages, use an existing shared/native data source where practical. If duplication is unavoidable, document it.

Maintain:

- `docs/EDITING_GUIDE.md` — human instructions for updating the site.
- `docs/CONTENT_MAP.md` — mapping from visible content to source files.

Update these docs whenever the editing model changes.

## Required page behavior

### About Me
Concise research-focused landing page. Use verified identity, affiliation/status, short bio, research interests, public social/contact links, and selected verified highlights. Avoid generic marketing language.

### Education
Support institution, degree, field, dates, location, GPA when desired, thesis, supervisor, coursework, and honors. Optional fields must disappear cleanly when empty.

### Research Experience
Support institution/lab, role, supervisor, dates, research problem, methods/contribution, outcome/status, and verified related links.

### Projects
Prefer al-folio project collection. Each project should support title, summary, date, tags/category, image, methods/tools, results, code/paper/demo links, related publication, and featured status.

### Publications
Use BibTeX/Jekyll Scholar. Populate only verified metadata. Highlight the site owner's author name using the template's supported configuration. Never create fake DOI/PDF/code links.

### CV
Use the template-supported CV renderer. Keep web CV readable. Publish a downloadable PDF only when a public-safe file is available.

## Design system

Preserve al-folio's academic character and light/dark mode.

Target:

- minimal, professional, research-first presentation;
- strong typography and whitespace;
- restrained accent color;
- consistent spacing/card/timeline language;
- responsive desktop/tablet/mobile layouts;
- semantic HTML and accessible interactions;
- descriptive alt text;
- no unnecessary animation;
- no giant hero;
- no excessive gradients or startup-style decoration.

## Change discipline

Before editing:

1. inspect relevant files;
2. check `git status`;
3. preserve unrelated user changes;
4. make the smallest coherent change;
5. avoid unnecessary dependencies.

After editing:

1. build/test using the repository-supported workflow;
2. inspect errors/warnings introduced by the change;
3. verify affected pages and navigation;
4. check light/dark mode when UI changed;
5. verify no demo content reappeared;
6. review `git diff`.

Do not claim a page or build works unless the available checks were actually run.

## Deployment rule

Do not push, publish, change GitHub Pages settings, or deploy unless the user explicitly requests it.

For a root GitHub Pages personal site, preserve al-folio's documented `url`/`baseurl` conventions. For project-page deployment, use the documented project `baseurl`.

## Collaboration model

The initial build creates a stable foundation. The user will later provide page-specific prompts.

For later page requests:

- preserve this content architecture unless there is a concrete reason to change it;
- implement only the requested page/change plus necessary shared adjustments;
- do not silently redesign unrelated pages;
- keep shared styles consistent;
- update editing documentation if needed;
- rebuild/test after each meaningful change.
