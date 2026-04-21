# AI Current State

## Version

`0.2.2`

## Implemented

- Native Home Assistant custom integration scaffold
- Single-instance config flow
- Native custom sidebar panel
- Static frontend bundle
- GET-only real data endpoints for:
  - overview
  - entities
  - devices
  - areas
  - integrations
  - relationships
- Admin-only enforcement for JSON data endpoints
- Compact backend shaping layer
- Best-effort masking for selected sensitive string patterns
- Tabbed frontend views with entity search/domain filtering
- Frontend API loading through the Home Assistant `hass.callApi` panel context
- Global frontend protected-data failure state for 401/403 auth failures
- Documentation and review baseline

## Confirmed Runtime State

In the user's tested Home Assistant runtime on the current working branch:

- The native custom panel loads successfully.
- The panel reports `Connected / Admin data endpoint available`.
- Overview loads real counts.
- Entities, devices, areas, integrations, and relationships load real items/link sets.
- The previous iframe-style invalid-auth failure is no longer the active observed behavior.

## Not implemented

- Floors full implementation
- Labels full implementation
- Dashboards full implementation
- Deep YAML or logic graphing
- Service exploration beyond future planning
- Write settings or saved preferences
- Any mutation feature

## Remaining Validation Caveat

The native panel auth bridge is confirmed in the user's tested runtime. It is not yet guaranteed across every Home Assistant version, frontend build mode, or deployment topology. If auth fails elsewhere, the UI still fails once and explains the protected-data failure without weakening endpoint auth.
