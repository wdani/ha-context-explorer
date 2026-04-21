# Changelog

## 0.2.0

- Replaced placeholder status/capabilities API responses with real read-only explorer endpoints for overview, entities, devices, areas, integrations, and relationships.
- Added authenticated, admin-only access checks for real Home Assistant data surfaces.
- Added compact backend shaping for Home Assistant state machine, registries, config entries, loaded components, and first relationship sets.
- Added best-effort mask-first privacy handling for obvious IPv4, MAC, and Wi-Fi-context values.
- Replaced the placeholder panel with tabbed views, overview counts, warnings, entity search/filtering, compact lists, and relationship summaries.
- Added lightweight AI/project documentation and a review bundle baseline.
- Bumped integration version metadata to `0.2.0`.

## 0.1.1

- Temporarily allowed the placeholder panel and placeholder demo endpoints to boot without Home Assistant auth.
- Kept the scaffold GET-only and read-only while no real Home Assistant data was exposed.

## 0.1.0

- Created the initial custom integration skeleton, sidebar panel shell, static assets, and minimal config flow.
