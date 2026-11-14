# Frontend — React/Vite historical yield dashboard

The checked frontend uses React 18, TypeScript, Vite 6, and lucide-react. [`src/App.tsx`](src/App.tsx) implements an accessible-style responsive dashboard with sidebar views (Overview, Yield prediction, Model insights), model-ready status, manual six-field input form, model metadata refresh, pending/error UI and unit-converted results. These are state-driven views rather than `react-router` URL routes.

## Running locally

```powershell
cd "D:\porto\100 day\day 37\frontend"
npm install
npm run build
npm run dev
```

Open `http://127.0.0.1:5173`; [`vite.config.ts`](vite.config.ts) proxies `/api` to `http://127.0.0.1:8000`. The backend must run separately. The browser fetches `/api/v1/model` and posts flat JSON to `/api/v1/predict`.

## User workflow

Select Overview or Yield prediction; enter `area`, `item`, `year`, rainfall, pesticides and average temperature; request an estimate; read hg/ha, kg/ha and tonnes/ha plus the disclaimer. Model insights shows saved held-out metrics from the API. The screenshot in `assets/screenshots/` proves the UI's model-online state, **not a successful predictive result**.

## Known gaps

Area and crop are free text, not validated dataset vocabulary selectors. There is no user account, time-series history, batch upload, map integration, online deployment, or data persistence in the reviewed source. The operational dashboard is a research prototype. See [API](../backend/README.md) and [limitations](../docs/en/limitations.md).
