"""Tests for the Ipswich integration."""

from custom_components.ipswich.client import parse_catalogue

CATALOGUE_FIXTURE = {
    "result": {
        "results": [
            {
                "name": "ipswich-cadastral",
                "title": "Ipswich Cadastral",
                "notes": "Cadastral boundaries",
                "resources": [{"url": "https://example.com/a.geojson"}],
            },
            {
                "name": "ipswich-parks-and-reserves",
                "title": "Ipswich Parks and Reserves",
                "notes": "Parks",
                "resources": [
                    {"url": "https://example.com/b.geojson"},
                    {"url": "https://example.com/c.geojson"},
                ],
            },
            {"name": "", "title": ""},
        ]
    }
}


def test_parse_catalogue_skips_empty_and_sorts() -> None:
    layers = parse_catalogue(CATALOGUE_FIXTURE)
    assert len(layers) == 2
    assert layers[0].title == "Ipswich Cadastral"
    assert layers[0].url == "https://data.gov.au/data/dataset/ipswich-cadastral"
    assert layers[1].resource_count == 2
