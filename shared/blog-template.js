/* ==========================================================================
   BRIGHTBOX DIGITAL — REUSABLE BLOG ARTICLE SCRIPT
   Version 1.0, adapted 2026-07-19.

   Goes in the site footer ONCE, not per article. Works on any page that
   contains a .bbx-post wrapper and does nothing on pages that do not.

   Degrades gracefully. With JavaScript blocked, every element is still
   fully readable, just without the motion and with the table of contents
   permanently open.
   ========================================================================== */
(function () {
  var root = document.querySelector('.bbx-post');
  if (!root) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Scroll reveal ---- */
  var revealEls = root.querySelectorAll('.bbx-post-reveal');
  if ('IntersectionObserver' in window && !reduceMotion) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('bbx-post-inview');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.16, rootMargin: '0px 0px -40px 0px' });
    Array.prototype.forEach.call(revealEls, function (el) { revealObserver.observe(el); });
  } else {
    Array.prototype.forEach.call(revealEls, function (el) { el.classList.add('bbx-post-inview'); });
  }

  /* ---- Table of contents accordion ---- */
  var tocToggle = root.querySelector('.bbx-post-tocHead');
  var tocPanel = root.querySelector('.bbx-post-tocPanel');
  if (tocToggle && tocPanel) {
    tocToggle.addEventListener('click', function () {
      var open = tocToggle.getAttribute('aria-expanded') === 'true';
      tocToggle.setAttribute('aria-expanded', String(!open));
      tocPanel.classList.toggle('bbx-post-tocOpen');
    });
  }

  /* ---- Active section tracking and smooth scroll ---- */
  var tocLinks = Array.prototype.slice.call(root.querySelectorAll('.bbx-post-tocList a'));
  var tracked = [];
  tocLinks.forEach(function (link) {
    var id = link.getAttribute('href').replace('#', '');
    var target = document.getElementById(id);
    if (target) tracked.push({ link: link, el: target });
  });

  function setActive(link) {
    tocLinks.forEach(function (l) { l.classList.remove('bbx-post-tocActive'); });
    link.classList.add('bbx-post-tocActive');
  }

  if (tracked.length && 'IntersectionObserver' in window) {
    var headingObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var match = tracked.filter(function (s) { return s.el === entry.target; })[0];
          if (match) setActive(match.link);
        }
      });
    }, { rootMargin: '-15% 0px -65% 0px' });
    tracked.forEach(function (s) { headingObserver.observe(s.el); });
    setActive(tracked[0].link);
  }

  tocLinks.forEach(function (link) {
    link.addEventListener('click', function (e) {
      var id = link.getAttribute('href').replace('#', '');
      var target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        var offsetTop = target.getBoundingClientRect().top + window.pageYOffset - 90;
        window.scrollTo({ top: offsetTop, behavior: reduceMotion ? 'auto' : 'smooth' });
      }
    });
  });
})();
