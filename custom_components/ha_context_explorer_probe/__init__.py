"""HA Context Explorer Probe integration."""
from __future__ import annotations

from pathlib import Path

from homeassistant.components import frontend
from homeassistant.components.http import HomeAssistantView
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from aiohttp import web

from .const import DOMAIN, NAME, PANEL_URL, STATIC_URL, VERSION


class ProbePanelView(HomeAssistantView):
    """Serve the panel HTML."""

    url = PANEL_URL
    name = f"{DOMAIN}:panel"
    requires_auth = False

    def __init__(self, html_path: str) -> None:
        self._html_path = html_path

    async def get(self, request: web.Request) -> web.Response:
        text = Path(self._html_path).read_text(encoding="utf-8")
        return web.Response(text=text.replace("{{VERSION}}", VERSION), content_type="text/html")


class ProbeStatusView(HomeAssistantView):
    """Read-only status endpoint."""

    url = f"/api/{DOMAIN}/status"
    name = f"api:{DOMAIN}:status"
    requires_auth = False

    async def get(self, request: web.Request) -> web.Response:
        return self.json(
            {
                "ok": True,
                "mode": "read_only_probe",
                "domain": DOMAIN,
                "version": VERSION,
                "writes_enabled": False,
                "service_calls_enabled": False,
                "state_changes_enabled": False,
            }
        )


class ProbeCapabilitiesView(HomeAssistantView):
    """Read-only capabilities endpoint."""

    url = f"/api/{DOMAIN}/capabilities"
    name = f"api:{DOMAIN}:capabilities"
    requires_auth = False

    async def get(self, request: web.Request) -> web.Response:
        return self.json(
            {
                "ui": {
                    "sidebar": True,
                    "custom_panel": True,
                    "mobile_ready": True,
                },
                "safety": {
                    "read_only": True,
                    "get_only": True,
                    "filesystem_writes": False,
                    "service_calls": False,
                    "state_mutation": False,
                    "sensitive_defaults": "mask_first",
                },
                "planned_scopes": [
                    "entities",
                    "devices",
                    "areas",
                    "integrations",
                    "relationships",
                ],
            }
        )


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the integration base."""
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the integration from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {}

    html_path = hass.config.path("custom_components", DOMAIN, "www", "panel.html")
    hass.http.register_view(ProbePanelView(html_path))
    hass.http.register_view(ProbeStatusView())
    hass.http.register_view(ProbeCapabilitiesView())

    static_path = str(hass.config.path("custom_components", DOMAIN, "www"))
    if hasattr(hass.http, "async_register_static_paths"):
        from homeassistant.components.http import StaticPathConfig

        await hass.http.async_register_static_paths(
            [StaticPathConfig(url_path=STATIC_URL, path=static_path, cache_headers=False)]
        )
    else:
        hass.http.register_static_path(STATIC_URL, static_path, False)

    frontend.async_register_built_in_panel(
        hass,
        component_name="iframe",
        sidebar_title=NAME,
        sidebar_icon="mdi:database-search",
        frontend_url_path=DOMAIN,
        config={"url": PANEL_URL},
        require_admin=True,
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload the integration."""
    frontend.async_remove_panel(hass, DOMAIN)
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return True
