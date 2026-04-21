# Review Bundle

## Scope

Phase 2 implements HA Context Explorer Probe `0.2.0` as the first real read-only explorer slice.

Implemented real data scopes:

- overview
- entities
- devices
- areas
- integrations
- relationships

Not implemented in this phase:

- floors
- labels
- dashboards
- deep YAML or logic graphing
- write settings or saved preferences
- mutation features

## Safety review

Result: pass with live-runtime caveat.

- Real data routes are registered as `GET` handlers only.
- JSON data endpoints set `requires_auth = True`.
- JSON data endpoints explicitly require `request["hass_user"].is_admin`.
- The panel shell remains boot-compatible, but it does not return real data.
- No service calls were added.
- No service registration was added.
- No POST / PUT / PATCH / DELETE handlers were added.
- No Home Assistant config writes were added.
- No `.storage` reads or writes were added.
- No secret access was added.
- No restart or supervisor controls were added.

## Privacy review

Result: pass with documented limitation.

- User-visible strings are shaped through best-effort masking.
- Masking covers obvious IPv4-like values, MAC-like values, and Wi-Fi / SSID / BSSID contexts where safely detectable.
- Numeric measurement values are preserved.
- Docs state that masking is best-effort and not guaranteed anonymization.
- No persistent privacy preference writing was added.

## Reference-data review

Result: pass with local git tooling caveat.

- `_local_reference/` remains listed in `.gitignore`.
- No implementation file reads from `_local_reference/`.
- No reference data was copied into repository source files or docs.
- Static scan outside `_local_reference/` found no copied local snapshot markers such as local instance name, location coordinates, HA version snapshot, registry filenames, or config allowlist keys.
- Local `git` was not available on PATH, so `git status` could not be used. No commit was made during this task.

## Validation commands

### Backend syntax

Command:

```powershell
python -c "import ast, pathlib; files=[pathlib.Path('custom_components/ha_context_explorer_probe/__init__.py'), pathlib.Path('custom_components/ha_context_explorer_probe/api.py'), pathlib.Path('custom_components/ha_context_explorer_probe/privacy.py'), pathlib.Path('custom_components/ha_context_explorer_probe/config_flow.py'), pathlib.Path('custom_components/ha_context_explorer_probe/const.py')]; [ast.parse(path.read_text(encoding='utf-8'), filename=str(path)) for path in files]; print('AST syntax OK for', len(files), 'backend files')"
```

Result:

```text
AST syntax OK for 5 backend files
```

### Manifest JSON

Command:

```powershell
python -c "import json, pathlib; json.loads(pathlib.Path('custom_components/ha_context_explorer_probe/manifest.json').read_text(encoding='utf-8')); print('manifest JSON OK')"
```

Result:

```text
manifest JSON OK
```

### Privacy helper sanity

Command:

```powershell
python -c "import importlib.util, pathlib; path=pathlib.Path('custom_components/ha_context_explorer_probe/privacy.py'); spec=importlib.util.spec_from_file_location('privacy_probe', path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); assert mod.mask_value('192.168.1.10') == '[masked-ipv4]'; assert mod.mask_value('aa:bb:cc:dd:ee:ff') == '[masked-mac]'; assert mod.mask_value('HomeNetwork', 'ssid') == '[masked-wifi]'; assert mod.mask_value(23.4, 'temperature') == 23.4; print('Privacy helper sanity OK')"
```

Result:

```text
Privacy helper sanity OK
```

### Safety scan

Command:

```powershell
Get-ChildItem -Recurse -File -Path custom_components\ha_context_explorer_probe | Select-String -Pattern "def post|def put|def patch|def delete|hass\.services\.async_call|async_register_service|register_admin_service|\.storage|secrets|hassTokens|localStorage|sessionStorage|Authorization|Bearer"
```

Result:

```text
No matches.
```

### Frontend asset and auth sanity

Commands confirmed:

- `panel.html` references `styles.css` and `app.js`.
- `panel.html` contains views for overview, entities, devices, areas, integrations, and relationships.
- `app.js` uses same-origin fetch:

```javascript
fetch(`${API_BASE}/${scope}`, { credentials: "same-origin" })
```

- `app.js` contains explicit 401 and 403 display handling.
- `app.js` does not reference `localStorage`, `sessionStorage`, `hassTokens`, `Authorization`, or `Bearer`.

### Version alignment

Confirmed `0.2.0` in:

- `custom_components/ha_context_explorer_probe/const.py`
- `custom_components/ha_context_explorer_probe/manifest.json`
- `README.md`
- `CHANGELOG.md`
- `docs/ai/AI_CURRENT_STATE.md`

Historical `0.1.1` and `0.1.0` references remain only in changelog/change-history context.

### Home Assistant runtime caveat

Command:

```powershell
python -c "import importlib.util; print('homeassistant available:', importlib.util.find_spec('homeassistant') is not None)"
```

Result:

```text
homeassistant available: False
```

Full live runtime behavior still needs validation inside Home Assistant, especially iframe auth behavior and current registry object compatibility.
