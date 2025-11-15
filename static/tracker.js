(function () {
  if (!localStorage.getItem("uid")) {
    localStorage.setItem("uid", "u_" + Math.random().toString(36).slice(2, 10));
  }

  const API = location.origin + "/api/events";

  function getDevice() {
    return {
      device_type: /Mobi|Android/i.test(navigator.userAgent) ? "mobile" : "desktop",
      browser: navigator.userAgent || null,
      platform: navigator.platform || null
    };
  }

  function send(eventName, metadata) {
    const payload = {
      event_name: eventName,
      user_id: localStorage.getItem("uid"),
      url: location.href,
      referrer: document.referrer || null,
      device: getDevice(),
      metadata: metadata || {}
    };

    // fire-and-forget
    if (navigator.sendBeacon) {
      const blob = new Blob([JSON.stringify(payload)], { type: "application/json" });
      navigator.sendBeacon(API, blob);
    } else {
      fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      }).catch(() => {});
    }
  }

  window.igot = { track: send };

  document.addEventListener("DOMContentLoaded", () => send("page_view"));
})();
