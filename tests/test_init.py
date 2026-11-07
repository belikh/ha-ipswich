"""Tests for the Ipswich integration."""

from custom_components.ipswich.client import parse_catalogue

CATALOGUE_FIXTURE = {
    "result": {
        "results": [
            {
                "name": "ipswich-traffic-signals",
                "title": "Ipswich Traffic Signals",
                "notes": "Signal locations and states",
                "resources": [{"url": "https://example.com/a.geojson"}],
            },
            {
                "name": "ipswich-cadastral",
                "title": "Ipswich Cadastral",
                "notes": "Static; must be filtered out",
                "resources": [{"url": "https://example.com/b.geojson"}],
            },
            {"name": "", "title": ""},
        ]
    }
}


def test_parse_catalogue_keeps_only_dynamic() -> None:
    layers = parse_catalogue(CATALOGUE_FIXTURE)
    assert len(layers) == 1
    assert layers[0].title == "Ipswich Traffic Signals"
    assert layers[0].url == "https://data.gov.au/data/dataset/ipswich-traffic-signals"
    assert layers[0].resource_count == 1
