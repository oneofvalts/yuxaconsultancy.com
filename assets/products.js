// yuxaconsultancy.com: the product tabs of the woodwork pages. The index
// beside (on narrow screens, above) the photographs lists the products; a
// click on one shows its photographs and hides the others', and the page
// address names it, so a link can open the page on that product. Without
// this script, the index links to the products, all shown one after the
// other.

(() => {
  const tabs = [...document.querySelectorAll(".shelf a.tab")];
  if (!tabs.length) return;

  const key = (hash) => decodeURIComponent(hash.slice(1));
  const panels = new Map(tabs.map((tab) => [key(tab.hash), document.getElementById(key(tab.hash))]));
  const smooth = () => (matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth");

  // Shows the product named, if there is one; whether there was.
  function select(name, scroll) {
    const panel = panels.get(name);
    if (!panel) return false;
    for (const tab of tabs) {
      if (key(tab.hash) !== name) {
        tab.removeAttribute("aria-current");
        continue;
      }
      tab.setAttribute("aria-current", "true");
      // Bring the tab into view inside the index, without moving the page.
      const shelf = tab.closest(".shelf");
      const box = shelf.getBoundingClientRect(), own = tab.getBoundingClientRect();
      shelf.scrollBy({
        left: own.left + own.width / 2 - (box.left + box.width / 2),
        top: own.top < box.top || own.bottom > box.bottom
          ? own.top + own.height / 2 - (box.top + box.height / 2) : 0,
        behavior: scroll ? smooth() : "auto",
      });
    }
    for (const [other, element] of panels) element.hidden = other !== name;
    if (scroll) panel.scrollIntoView({ block: "start", behavior: smooth() });
    return true;
  }

  for (const tab of tabs) {
    tab.addEventListener("click", (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      select(key(tab.hash), true);
      history.replaceState(history.state, "", tab.hash);
    });
  }
  addEventListener("hashchange", () => select(key(location.hash), true));
  if (!select(key(location.hash), false)) select(key(tabs[0].hash), false);
})();
