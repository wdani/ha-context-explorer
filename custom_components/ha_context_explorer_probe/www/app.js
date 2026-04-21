async function loadJson(url, targetId) {
  const target = document.getElementById(targetId);
  try {
    const response = await fetch(url, { credentials: "same-origin" });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const data = await response.json();
    target.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    target.textContent = `Failed to load ${url}\n${String(error)}`;
  }
}

loadJson("/api/ha_context_explorer_probe/status", "status");
loadJson("/api/ha_context_explorer_probe/capabilities", "capabilities");
