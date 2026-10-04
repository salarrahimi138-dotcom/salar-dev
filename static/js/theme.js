(function () {

    const root = document.documentElement;
    const toggle = document.getElementById("theme-toggle");

    if (!toggle) return;


    function applyTheme(theme) {

        root.setAttribute("data-theme", theme);

        // checked = dark
        toggle.checked = theme === "dark";

        localStorage.setItem("theme", theme);
    }


    const savedTheme = localStorage.getItem("theme");


    if (savedTheme) {
        applyTheme(savedTheme);
    } else {
        applyTheme("dark");
    }


    toggle.addEventListener("change", function () {

        applyTheme(toggle.checked ? "dark" : "light");

    });


})();