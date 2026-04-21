# HA Context Explorer Probe

A separate experimental Home Assistant custom integration with its own sidebar UI.

This is **not** a continuation of `ha-ai-context-exporter`.
It is a clean prototype that explores a different direction:

- native Home Assistant integration
- custom sidebar panel UI
- admin-only access
- strict read-only design
- no service calls
- no state changes
- no file writes
- privacy-first defaults

## Current scope

This starter scaffold provides:

- a Home Assistant custom integration skeleton
- a sidebar panel
- a minimal read-only HTTP API
- a standalone frontend UI served by the integration
- explicit architectural boundaries for future work

## What it does right now

- registers a sidebar entry called **Context Explorer Probe**
- serves a small frontend app
- exposes a read-only status endpoint
- exposes a read-only capabilities endpoint
- keeps all routes GET-only

## What it does not do yet

- no live entity export
- no device/area/integration context loading
- no authentication/token extension logic beyond normal HA auth requirements
- no config flow
- no options flow
- no file system inspection
- no secret access
- no writing anywhere

## Suggested next steps

1. Replace the placeholder capabilities payload with real read-only data sources.
2. Add a compact entity browser endpoint.
3. Add masking defaults before exposing any sensitive values.
4. Add tabs for entities, integrations, devices, areas, and relationships.
5. Keep all future backend routes GET-only.

## Installation (manual prototype)

1. Copy `custom_components/ha_context_explorer_probe` into your Home Assistant `custom_components` directory.
2. Restart Home Assistant.
3. Add the integration from **Settings -> Devices & Services**.
4. Open the new sidebar entry.

## Honest limitation

This scaffold was created outside a live Home Assistant runtime and was not validated inside your HA instance yet.


## 0.1.1 auth note
- The initial 0.1.0 starter used authenticated iframe panel access and could trigger `invalid authentication` on `/ha_context_explorer_probe/panel` in Home Assistant.
- The 0.1.1 starter temporarily serves the placeholder panel and placeholder demo endpoints without HA auth so the UI can boot inside the built-in iframe panel.
- This is acceptable only because the current endpoints expose placeholder, non-sensitive demo data. Before wiring real Home Assistant data, auth must be hardened again with a proper panel-token/auth bridge or manual validation approach.
