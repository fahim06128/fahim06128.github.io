# Portfolio Site Rules and Guidelines

These rules apply to developing, updating, and maintaining this `al-folio` (v1.x) personal portfolio website.

## Core Architecture & Boundaries

- **Starter vs. Gem Architecture:**
  - `al-folio` v1.x is a thin Jekyll starter. Runtime behavior (layouts, includes, Sass, Liquid tags, filters, and feature JS) resides in external gems under `al-org-dev`.
  - Refer to `AGENTS.md` and `docs/BOUNDARIES.md` before making structural changes.
  - Do not create gem-owned directories (`_layouts/`, `_includes/`, `_sass/`, `_scripts/`, `assets/tailwind/`, `tailwind.config.js`, `assets/webfonts/`) directly in this repo unless explicitly creating a documented local override.

## Change Routing

- **Site Configuration & Metadata:**
  - Edit `_config.yml` for site details (name, title, contact note, social links, feature toggles, etc.).
- **Dependencies & Plugins:**
  - Updates require editing **both** `Gemfile` (under `group :al_folio_plugins`) and `_config.yml` (under `plugins:`). Both lists must stay in sync.
- **Content Collections:**
  - Biography and bio details: `_pages/about.md` and `_data/`
  - Projects: `_projects/`
  - Blog posts: `_posts/`
  - News/announcements: `_news/`
  - Publications/bibliography: `_bibliography/papers.bib` and `_pages/publications.md`
  - Teaching: `_teachings/` or `_pages/teaching.md`
  - CV: `_pages/cv.md` or data files for rendercv
- **Static Assets:**
  - Images, PDFs, and media belong in `assets/img/`, `assets/pdf/`, etc.

## Best Practices & Failure Modes

1. **Feature Gating:**
   - Features fail silently if their gem is not loaded, their feature flag is false in `_config.yml`, or the page frontmatter lacks the opt-in flag.
2. **Base URL Awareness:**
   - Always verify the effective `baseurl` in `_config.yml` when generating links or running local builds (`bundle exec jekyll build --baseurl /al-folio` or as configured).
3. **Validation & Linting:**
   - Run Prettier formatting before completing tasks: `npm run lint:prettier` (or `npx prettier . --write`).
   - Run style contract checks: `npm run lint:style-contract`.
   - Verify the site builds cleanly: `bundle exec jekyll build`.

## Tone and Content Conventions

- Keep personal, professional, and academic content accurate and up to date.
- Maintain documentation integrity and preserve existing custom configurations.
