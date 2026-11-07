# Ipswich City Council

Home Assistant integration for **Ipswich City Council** — Queensland, Australia.

Everything in here comes from the council's public open data
(token-free, no API keys, no add-ons).

## What you get

- **All datasets** — every published dataset becomes a sensor showing its resource/feature count and source URL.
- **Waste collection days** (where openly published) — next bin collection + "put bins out tonight?" for one address/property.

## Data source

data.gov.au CKAN (68 datasets, token-free). Waste is NOT in open data (only via the council Bin App), so v1 is catalogue-only.

## Install (HACS)

1. Add a custom repository: `https://github.com/belikh/ha-ipswich` as type **Integration**.
2. Install **Ipswich City Council** and restart Home Assistant.
3. Add the integration and choose: all layers / waste / single layer.

## Development

```bash
uv sync
uv run pytest
uv run ruff check .
uv run mypy
```

Licence: MIT. Data © Ipswich City Council (Creative Commons). Unofficial; not endorsed by the council.


## v0.1.1 — Curated: superseded/LIDAR/contours/DTM/aerial datasets removed — 68 -> 22 sensors.


## Live status reality check

Ipswich open data contains essentially no live status feeds — only
locations (e.g. Traffic Signals). Under the status-only rule there is
nothing meaningful to expose beyond "no live status available in open
data". The v0.3.0 bundle therefore adds **no new sensors** for
Ipswich; the catalogue stays at Traffic Signals only.
