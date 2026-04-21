# AI Current State

## Version

`0.2.0`

## Implemented

- Native Home Assistant custom integration scaffold
- Single-instance config flow
- Sidebar iframe panel
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
- Documentation and review baseline

## Not implemented

- Floors full implementation
- Labels full implementation
- Dashboards full implementation
- Deep YAML or logic graphing
- Service exploration beyond future planning
- Write settings or saved preferences
- Any mutation feature

## Known validation gap

Local syntax and static checks are useful, but live Home Assistant runtime testing is still required to confirm iframe auth behavior and registry compatibility across HA versions.
