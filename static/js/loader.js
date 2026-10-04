(function () {
  const MIN_TIME = 1500; 
  const startTime = Date.now();
  const loader = document.getElementById("page-loader");

  if (!loader) return;

  window.addEventListener("load", function () {
    const elapsed = Date.now() - startTime;
    const wait = Math.max(0, MIN_TIME - elapsed);

    setTimeout(function () {
      loader.classList.add("hidden");

      loader.addEventListener("transitionend", function () {
        loader.remove();
      });
    }, wait);
  });
})();