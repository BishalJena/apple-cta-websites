// Dayline — small progressive enhancements. The site works without this file.
(function () {
  // Deterministic pseudo-random so the grids look the same on every load.
  function rng(seed) {
    let s = seed >>> 0;
    return function () {
      s = (s * 1664525 + 1013904223) >>> 0;
      return s / 4294967296;
    };
  }

  // Fill every .grid[data-cells] with habit-tracker squares.
  document.querySelectorAll(".grid[data-cells]").forEach(function (grid, idx) {
    const cells = parseInt(grid.dataset.cells, 10);
    const density = parseFloat(grid.dataset.density || "0.65");
    const rand = rng((parseInt(grid.dataset.seed, 10) || idx + 1) * 9973);
    const frag = document.createDocumentFragment();
    for (let i = 0; i < cells; i++) {
      const cell = document.createElement("i");
      // Streaks get denser toward the end, like a habit taking hold.
      const bias = density + (i / cells) * 0.25;
      if (rand() < bias) cell.style.setProperty("--a", Math.round(45 + rand() * 55) + "%");
      frag.appendChild(cell);
    }
    grid.appendChild(frag);
  });

  // Hero phone: check habits off one after another, on a loop.
  const checks = Array.from(document.querySelectorAll(".phone .board-check"));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (checks.length && !reduceMotion) {
    let step = 0;
    setInterval(function () {
      if (step < checks.length) {
        const check = checks[step];
        check.classList.add("done");
        const grid = check.closest(".board").querySelector(".grid");
        const last = grid && grid.lastElementChild;
        if (last) last.style.setProperty("--a", "100%");
      } else if (step === checks.length + 2) {
        checks.forEach(function (c) {
          c.classList.remove("done");
          const last = c.closest(".board").querySelector(".grid i:last-child");
          if (last) last.style.setProperty("--a", "10%");
        });
        step = -1;
      }
      step++;
    }, 1100);
  } else {
    checks.forEach(function (c) { c.classList.add("done"); });
  }

  // Fade sections in as they scroll into view.
  const revealables = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    const io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: "0px 0px -60px 0px" });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add("in"); });
  }

  // Forms: if no real endpoint is configured (action="#"), fall back to a
  // friendly local confirmation (or mailto for the contact form).
  document.querySelectorAll("form[data-form]").forEach(function (form) {
    if (form.getAttribute("action") !== "#") return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (form.dataset.form === "contact") {
        const data = new FormData(form);
        const to = form.dataset.mailto;
        const subject = encodeURIComponent((data.get("topic") || "Hello") + " — Dayline");
        const body = encodeURIComponent((data.get("message") || "") + "\n\n— " + (data.get("name") || "") + " <" + (data.get("email") || "") + ">");
        window.location.href = "mailto:" + to + "?subject=" + subject + "&body=" + body;
      }
      const ok = form.parentElement.querySelector(".success");
      if (ok) ok.classList.add("show");
      form.reset();
    });
  });

  // Keep the copyright year current.
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
