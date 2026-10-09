// Lotus waitlist sites — small progressive enhancements.
// Generated into each app folder by tools/site-builder/build.py.
// Every page works without this file; forms fall back to plain POSTs.
(function () {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Deterministic pseudo-random so generated grids look the same on every load.
  function rng(seed) {
    let s = seed >>> 0;
    return function () {
      s = (s * 1664525 + 1013904223) >>> 0;
      return s / 4294967296;
    };
  }

  document.querySelectorAll(".grid[data-cells]").forEach(function (grid, idx) {
    const cells = parseInt(grid.dataset.cells, 10);
    const density = parseFloat(grid.dataset.density || "0.65");
    const rand = rng((parseInt(grid.dataset.seed, 10) || idx + 1) * 9973);
    const frag = document.createDocumentFragment();
    for (let i = 0; i < cells; i++) {
      const cell = document.createElement("i");
      const bias = density + (i / cells) * 0.25;
      if (rand() < bias) cell.style.setProperty("--a", Math.round(45 + rand() * 55) + "%");
      frag.appendChild(cell);
    }
    grid.appendChild(frag);
  });

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

  // ---------- Waitlist ----------
  // The endpoint lives in <meta name="waitlist-endpoint">, set per build.
  const endpointMeta = document.querySelector('meta[name="waitlist-endpoint"]');
  const endpoint = endpointMeta ? endpointMeta.content.trim() : "";

  function setStatus(form, kind, text) {
    const status = form.parentElement.querySelector(".waitlist-status");
    if (!status) return;
    status.className = "waitlist-status " + kind;
    const icon = kind === "ok" ? "check_circle" : kind === "err" ? "error" : "";
    status.innerHTML = (icon ? '<span class="icon">' + icon + "</span>" : "") + "<span></span>";
    status.lastChild.textContent = text;
  }

  document.querySelectorAll("form[data-waitlist]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const data = new FormData(form);
      const email = String(data.get("email") || "").trim();
      if (!email || !form.checkValidity()) {
        setStatus(form, "err", "Please enter a valid email address.");
        return;
      }
      if (data.get("company")) return; // honeypot filled: quietly ignore bots
      if (!endpoint) {
        setStatus(form, "err", "The waitlist isn't connected yet. Please check back soon.");
        return;
      }
      const button = form.querySelector("button");
      button.disabled = true;
      fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify({ email: email, app: form.dataset.app, source: form.dataset.source || "site" }),
      })
        .then(function (res) {
          return res.json().catch(function () { return {}; }).then(function (body) {
            if (!res.ok) throw new Error(body.error || "Something went wrong. Please try again.");
            return body;
          });
        })
        .then(function (body) {
          setStatus(form, "ok", body.already
            ? "You're already on the list. We'll be in touch."
            : "You're on the list! We'll email you when it's ready.");
          form.reset();
        })
        .catch(function (err) {
          setStatus(form, "err", err.message || "Something went wrong. Please try again.");
        })
        .finally(function () { button.disabled = false; });
    });
  });

  // Returning from a no-JS form post (?joined=1).
  if (/[?&]joined=1/.test(location.search)) {
    document.querySelectorAll("form[data-waitlist]").forEach(function (form) {
      setStatus(form, "ok", "You're on the list! We'll email you when it's ready.");
    });
  }

  // ---------- Contact form → mail app ----------
  document.querySelectorAll("form[data-form=contact]").forEach(function (form) {
    if (form.getAttribute("action") !== "#") return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const data = new FormData(form);
      const subject = encodeURIComponent((data.get("topic") || "Hello") + " — " + form.dataset.appName);
      const body = encodeURIComponent((data.get("message") || "") + "\n\n— " + (data.get("name") || "") + " <" + (data.get("email") || "") + ">");
      window.location.href = "mailto:" + form.dataset.mailto + "?subject=" + subject + "&body=" + body;
      const ok = form.parentElement.querySelector(".success");
      if (ok) ok.classList.add("show");
    });
  });

  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
