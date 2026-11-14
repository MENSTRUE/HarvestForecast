# Documentation change report — HarvestForecast

## Scope

Documentation-only package prepared from the GitHub `main` repository tree and inspected source/report files on 2026-11-14. Replaces root `README.md` and `AGENTS.md` **when installed**, adds matched English/Indonesian detailed guides and component READMEs/AGENTS. The installer must **not** modify source code, notebooks, trained models, dataset files, `LICENSE`, or images.

## Verification highlights

- Backend source verified to extract nested `artifact['model']`; model is a joblib dictionary.
- Evidence reports confirm data audit (25,932 → 13,130), time split (8,444/2,331/2,355), validation winner `random_forest_120`, held-out MAE 16,393.5078 hg/ha and R² 0.874259.
- Source licensing and upstream Zenodo equivalence remain unverified.
- Local application screenshot documents model online only; no verified submitted prediction, public deployment, or farm validation.
- Original `reports/extracted/MODEL_CARD.md` and `docs/FULLSTACK_SETUP.md` are retained.
- Repository contains a tracked `backend/app/main.py.backup_20261114_212553` and `frontend/tsconfig.tsbuildinfo` that merit later Git hygiene review; this package does **not** delete them.
- Existing root `LICENSE` says a license has not been selected. Documentation does not silently assign one.

## Recommended review

After safe installation: `git diff --check`, `git diff --stat`, inspect README images on GitHub, verify backlinks, and independently run `npm run build` plus representative API tests before release claims. Commit suggestion: `docs: document HarvestForecast experiment and local application bilingually`.
