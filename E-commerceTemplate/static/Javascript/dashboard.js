document.addEventListener("DOMContentLoaded", function () {
  const profileBtn = document.querySelector(".profile-btn");
  const dropdown = document.getElementById("profileDropdown");

  if (!profileBtn || !dropdown) return;

  function openDropdown() {
    dropdown.classList.add("open");
    dropdown.setAttribute("aria-hidden", "false");
    profileBtn.setAttribute("aria-expanded", "true");
  }

  function closeDropdown() {
    dropdown.classList.remove("open");
    dropdown.setAttribute("aria-hidden", "true");
    profileBtn.setAttribute("aria-expanded", "false");
  }

  profileBtn.addEventListener("click", function (e) {
    e.stopPropagation();
    if (dropdown.classList.contains("open")) {
      closeDropdown();
    } else {
      openDropdown();
    }
  });

  // Close when clicking outside
  document.addEventListener("click", function (e) {
    if (!dropdown.contains(e.target) && !profileBtn.contains(e.target)) {
      closeDropdown();
    }
  });

  // Close on Escape
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeDropdown();
    }
  });

  // DARK MODE: persist and apply theme
  const darkToggle = document.getElementById("darkModeToggle");
  const darkLabel = document.querySelector(".dark-mode-label");

  function setLabelForTheme(theme) {
    if (!darkLabel) return;
    // When dark theme is active show 'Light' so clicking it will switch to light
    darkLabel.textContent = theme === "dark" ? "Light" : "Dark";
  }

  function applyTheme(theme) {
    if (!darkToggle) return;
    if (theme === "dark") {
      document.body.classList.add("dark-theme");
      darkToggle.checked = true;
    } else {
      document.body.classList.remove("dark-theme");
      darkToggle.checked = false;
    }
    setLabelForTheme(theme);
  }

  // initialize theme from localStorage or system preference
  (function initTheme() {
    if (!darkToggle) return;
    const stored = localStorage.getItem("theme");
    if (stored) {
      applyTheme(stored);
    } else {
      const prefersDark =
        window.matchMedia &&
        window.matchMedia("(prefers-color-scheme: dark)").matches;
      applyTheme(prefersDark ? "dark" : "light");
    }
  })();

  if (darkToggle) {
    darkToggle.addEventListener("change", function () {
      const theme = darkToggle.checked ? "dark" : "light";
      applyTheme(theme);
      localStorage.setItem("theme", theme);
    });
  }
});
