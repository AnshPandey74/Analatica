(function () {
  if (!localStorage.getItem("uid")) {
    localStorage.setItem("uid", "u_" + Math.random().toString(36).slice(2, 10));
  }

  const API = location.origin + "/api/events";

  function getDevice() {
    return {
      device_type: /Mobi|Android/i.test(navigator.userAgent) ? "mobile" : "desktop"
    };
  }

  function send(eventName, metadata) {
    const payload = {
      event_name: eventName,
      user_id: localStorage.getItem("uid"),
      device: getDevice(),
      metadata: metadata || {}
    };

    fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
  }

  window.igot = { track: send };

  document.addEventListener("DOMContentLoaded", () => send("page_view"));
})();
