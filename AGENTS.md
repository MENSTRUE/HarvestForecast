# AGENTS — HarvestForecast Day 37

## Mission and source-of-truth priority

Maintain an auditable **historical yield regression** prototype, not a claim of live preseason forecasting. Source precedence: (1) executed notebook + original experiment JSON/CSV in `reports/extracted`, (2) checked runtime `backend/app/main.py` and `frontend/src/App.tsx`, (3) human documentation, (4) proposals. Do not overwrite or conceal source contradictions.

## Repository invariants

Preserve `README.md`, `AGENTS.md`, `LICENSE`, `.gitignore`, `.env.example`, `notebooks/`, `models/`, `reports/`, `assets/{plots,examples,screenshots,diagrams}`, `backend/`, `frontend/`, `docs/`, `scripts/`. Do not create tracked `datasets/` or commit raw CSV inputs, archives, caches, environments, credentials or unexpected model binaries. Existing `LICENSE` states license not yet selected; do not pretend it grants redistribution rights. Do not delete reports or modify notebooks/model/checkpoints without authorization.

## Before → Now → Next

Before: inspect five source files, clean repeated area/crop/year keys, establish temporal splits and baseline. Now: saved Random Forest pipeline, reported held-out evaluation, running local API/UI as demonstrated, but no independent prediction or public deployment evidence. Next: verified positive/negative API tests, category vocabulary validation, prospective feature availability, geographic OOD evaluation, provenance/license reconciliation, then production assessment.

## ML research rules

Reproduce the notebook with source hashes/seed. Train-only preprocessing; validation-only champion selection. Held-out test is not a hyperparameter tuning resource. Distinguish a saved test result from a blind prospective evaluation. Never invent sample sizes, test scores, field results or calibrated uncertainty. Six exact ordered feature names; target `value_hg_ha` (hg/ha); regression, not classification. Treat unknown categories and temporal covariates as major reliability risks. Document sources, versions, permissions and any train/validation/test leakage checks.

## Backend and frontend

Backend: load only trusted joblib bundle dictionary; extract `artifact['model']`; validate feature order and unit; use typed request validation, safe error handling and restricted local CORS. Frontend: keep six exact inputs, display units/disclaimer, handle errors and backend absence; never fake results. Review responsive UI and `npm run build`. Do not claim offline/online deployment capabilities without tests. Coordinate API changes across code and docs.

## Security, integrity and Git

No untrusted pickle execution, secrets, arbitrary URLs to load models, unreviewed data publication, or silent rewrites. Backup existing docs before replacement; inspect `git diff`; never force-push or alter tracked generated artifacts unasked. Remove accidental backup/code build files only after explicit review. Use `docs(en/id)` with equal coverage and no broken relative links. Require evidence for every number and image; test docs paths, Python syntax and frontend builds where tools are available.

## Definition of done

Changes are complete only when: tests match actual implementation; metrics reconcile with JSON/CSV; sample inputs respect training contract; research limitations remain visible; both languages are synchronized; links and figures resolve; no raw input datasets or credentials are committed; `git diff --check` passes; reviewer can identify unresolved uncertainties. Prefer `docs: ...`, `fix: ...`, `feat: ...` commit titles.

[Backend rules](backend/AGENTS.md) · [Frontend rules](frontend/AGENTS.md) · [Documentation index](docs/README.md)
