.. raw:: html

   <p align="right">
     <picture>
       <source media="(prefers-color-scheme: dark)" srcset="https://github.com/belikh/design/releases/latest/download/logo-dark.svg">
       <img alt="jupiter.au" src="https://github.com/belikh/design/releases/latest/download/logo-light.svg" width="260">
     </picture>
   </p>

   <h1>Ipswich City Council</h1>

.. meta::
   :description: Home Assistant integration that turns datasets from the Ipswich City Council open data listing on data.gov.au into sensors.

Home Assistant integration that turns datasets from the Ipswich City Council open data listing on data.gov.au into sensors. It needs no API key.

|

.. raw:: html

   <p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github.com/belikh/design/releases/latest/download/rule-end-dark.svg"><img alt="" src="https://github.com/belikh/design/releases/latest/download/rule-end-light.svg" width="50%"></picture></p>

Install
-------

1. In HACS, add a custom repository: ``https://github.com/belikh/ha-ipswich``, type **Integration**.
2. Install **Ipswich City Council** and restart Home Assistant.
3. Go to **Settings > Devices & Services > Add integration** and pick **Ipswich City Council**.

|

Use
---

The integration reads the ``city-of-ipswich`` organisation on the data.gov.au CKAN API and creates one sensor per dataset. The state is the number of resources in the dataset. The attributes are ``layer_title``, ``source_url`` and ``feature_count``.

The catalogue is filtered to datasets that change over time. Datasets whose titles do not match the integration's list of live-data keywords, and historical datasets, are skipped.

.. raw:: html

   <table>
     <tr align="left"><th>Note</th></tr>
     <tr><td>

Ipswich does not publish bin collection days as open data (they are only in the council's Bin App), so there are no waste sensors.

.. raw:: html

   </td></tr>
   </table>

|

Configuration
-------------

The refresh interval is set at setup and can be changed later under **Configure** on the integration card. It defaults to 6 hours and accepts 1 to 48.

|

Develop
-------

.. code-block:: sh

   uv sync
   uv run pytest
   uv run ruff check .
   uv run mypy

|

.. raw:: html

   <p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="https://github.com/belikh/design/releases/latest/download/rule-end-dark.svg"><img alt="" src="https://github.com/belikh/design/releases/latest/download/rule-end-light.svg" width="50%"></picture></p>

Licence
-------

MIT. Data (c) Ipswich City Council, Creative Commons. Unofficial; not endorsed by the council.

|

.. raw:: html

   <p align="right"><sub>jupiter.au</sub></p>

