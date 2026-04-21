# AI Change History

## 0.2.0

Phase 2 turned the starter into a first real read-only explorer slice.

Key changes:

- Added authenticated admin-only GET endpoints for overview, entities, devices, areas, integrations, and relationships.
- Added a backend shaping layer so the UI consumes stable compact JSON instead of raw Home Assistant objects.
- Added mask-first privacy helpers for obvious IPv4, MAC, and Wi-Fi-context strings.
- Replaced the placeholder panel with tabbed views and honest auth/unavailable handling.
- Added project docs, changelog, and review bundle.

Important boundaries kept:

- no service calls
- no mutation endpoints
- no Home Assistant config writes
- no `.storage` reads or writes
- no secret access
- no copied local reference data

## 0.1.1

The placeholder panel temporarily allowed unauthenticated booting because no real Home Assistant data was exposed. That is no longer acceptable for real data endpoints.

## 0.1.0

Initial standalone custom integration and panel scaffold.
