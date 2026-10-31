// yuxaconsultancy.com: the photo viewer of the work pages, the site's only
// script. A click on a photograph of the gallery shows it in the page's
// viewer dialog, as large as the window allows, with its caption. The
// buttons, the arrow keys and a sideways swipe turn to the previous or next
// photograph; the close button, Escape, a click beside the photograph, a
// swipe down and the browser's back button close the viewer. Without this
// script, each photograph's link opens its 2000 px copy.

(() => {
  const viewer = document.querySelector("dialog.viewer");
  const figures = document.querySelectorAll(".gallery figure");
  if (!viewer || !viewer.showModal || !figures.length) return;

  const frame = viewer.querySelector(".frame");
  const text = viewer.querySelector(".text");
  const count = viewer.querySelector(".count");
  const photos = [...figures].map((figure) => ({
    link: figure.querySelector("a"),
    copy: figure.querySelector("img").src,
    caption: figure.querySelector("figcaption").textContent,
    ratio: figure.style.getPropertyValue("--r"),
  }));
  const at = (i) => (i + photos.length) % photos.length;
  let current = 0;
  // Whether opening the viewer added an entry to the history: the back
  // button then closes the viewer instead of leaving the page.
  let pushed = false;

  function show(i) {
    current = at(i);
    const photo = photos[current];
    const img = new Image();
    img.alt = photo.caption;
    img.style.setProperty("--r", photo.ratio);
    // The page's copy fills the box until the large one has arrived.
    img.style.backgroundImage = `url("${photo.copy}")`;
    img.src = photo.link.href;
    img.addEventListener("load", () => {
      for (const j of [current + 1, current - 1]) new Image().src = photos[at(j)].link.href;
    }, { once: true });
    frame.replaceChildren(img);
    text.textContent = photo.caption;
    count.textContent = `${current + 1} / ${photos.length}`;
  }

  photos.forEach((photo, i) => {
    photo.link.addEventListener("click", (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      show(i);
      viewer.showModal();
      history.pushState({ viewer: true }, "");
      pushed = true;
    });
  });

  viewer.querySelector(".close").addEventListener("click", () => viewer.close());
  viewer.querySelector(".prev").addEventListener("click", () => show(current - 1));
  viewer.querySelector(".next").addEventListener("click", () => show(current + 1));
  viewer.addEventListener("click", (event) => {
    if (event.target === viewer || event.target === frame) viewer.close();
  });
  viewer.addEventListener("keydown", (event) => {
    const step = { ArrowLeft: -1, ArrowRight: 1 }[event.key];
    if (!step) return;
    event.preventDefault();
    show(current + step);
  });

  // Swipes of one finger; with the page zoomed in, the finger pans instead.
  let start = null;
  viewer.addEventListener("touchstart", (event) => {
    const [touch] = event.touches;
    start = event.touches.length === 1 ? { x: touch.clientX, y: touch.clientY } : null;
  }, { passive: true });
  viewer.addEventListener("touchend", (event) => {
    if (!start || window.visualViewport?.scale > 1) return;
    const [touch] = event.changedTouches;
    const dx = touch.clientX - start.x, dy = touch.clientY - start.y;
    start = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > 2 * Math.abs(dy)) show(current + (dx < 0 ? 1 : -1));
    else if (dy > 80 && dy > 2 * Math.abs(dx)) viewer.close();
  }, { passive: true });

  viewer.addEventListener("close", () => {
    frame.replaceChildren();
    if (pushed) {
      pushed = false;
      history.back();
    }
  });
  addEventListener("popstate", () => {
    if (pushed) {
      pushed = false;
      viewer.close();
    }
  });
})();
