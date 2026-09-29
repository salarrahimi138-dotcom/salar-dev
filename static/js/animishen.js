(function () {
    var root = document.documentElement;
    root.classList.add('js');

    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var SELECTOR = '.reveal, .reveal-left, .reveal-right';

    function finish(el) {
        el.classList.remove('reveal', 'reveal-left', 'reveal-right', 'show');
        Array.prototype.slice.call(el.classList).forEach(function (c) {
            if (/^delay-\d+$/.test(c)) el.classList.remove(c);
        });
        el.style.removeProperty('transition-delay');
    }

    function hasDelayClass(el) {
        return Array.prototype.some.call(el.classList, function (c) {
            return /^delay-\d+$/.test(c);
        });
    }

    function init() {
        var items = document.querySelectorAll(SELECTOR);
        if (!items.length) return;

        if (reduce || !('IntersectionObserver' in window)) {
            items.forEach(finish);
            return;
        }

        var groups = new Map();
        items.forEach(function (el) {
            var count = groups.get(el.parentElement) || 0;
            if (!hasDelayClass(el)) {
                el.style.transitionDelay = Math.min(count, 6) * 80 + 'ms';
            }
            groups.set(el.parentElement, count + 1);
        });

        var io = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (!entry.isIntersecting) return;
                    var el = entry.target;
                    io.unobserve(el);
                    el.classList.add('show');

                    var done = false;
                    function cleanup() {
                        if (done) return;
                        done = true;
                        finish(el);
                    }
                    el.addEventListener('transitionend', function (e) {
                        if (e.propertyName === 'transform') cleanup();
                    });
                    setTimeout(cleanup, 1600);
                });
            },
            { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
        );

        items.forEach(function (el) {
            io.observe(el);
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();