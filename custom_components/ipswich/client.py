"""CKAN client for Ipswich City Council (data.gov.au).

Every endpoint here is token-free. Ipswich publishes its open
datasets on the Australian Government portal (data.gov.au, CKAN);
licence: Creative Commons Attribution (CC BY).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from aiohttp import ClientSession

from .const import CATALOGUE_URL, CKAN_ORG


@dataclass(frozen=True)
class LayerDefinition:
    """One published Ipswich dataset."""

    title: str
    url: str
    description: str = ""
    resource_count: int = 0


@dataclass
class CatalogueResult:
    """Result of a catalogue fetch."""

    layers: list[LayerDefinition] = field(default_factory=list)


DYNAMIC_TITLE_SUBSTRINGS = (
    "traffic signal",
)


def is_junk_title(title: str) -> bool:
    """Return True if a dataset is not dynamic (kept whitelist) or historical."""
    lowered = title.lower()
    if "historical" in lowered:
        return True
    return not any(token in lowered for token in DYNAMIC_TITLE_SUBSTRINGS)


def parse_catalogue(payload: dict[str, Any]) -> list[LayerDefinition]:
    """Parse a CKAN package_search payload into layers.

    Pure function (no I/O) so it can be unit-tested with fixtures.
    """
    layers: list[LayerDefinition] = []
    result = payload.get("result") or {}
    for item in result.get("results") or []:
        name = str(item.get("name") or "").strip()
        title = str(item.get("title") or name).strip()
        if not name:
            continue
        if is_junk_title(title):
            continue
        description = str(item.get("notes") or "").strip()
        resources = item.get("resources") or []
        layers.append(
            LayerDefinition(
                title=title,
                url=f"https://data.gov.au/data/dataset/{name}",
                description=description,
                resource_count=len(resources),
            )
        )
    layers.sort(key=lambda item: item.title.lower())
    return layers


class IpswichClient:
    """Thin async client for Ipswich City Council CKAN data."""

    def __init__(self, session: ClientSession) -> None:
        """Initialise with a shared aiohttp session."""
        self._session = session

    async def fetch_catalogue(self) -> list[LayerDefinition]:
        """Fetch and parse the catalogue for the Ipswich organisation."""
        async with self._session.get(
            CATALOGUE_URL,
            params={"q": f"organization:{CKAN_ORG}", "rows": "1000"},
        ) as response:
            response.raise_for_status()
            payload = await response.json()
        return parse_catalogue(payload)

    async def query_layer_count(self, definition: LayerDefinition) -> int:
        """Return the resource count for one dataset."""
        return definition.resource_count
