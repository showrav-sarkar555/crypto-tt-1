// ===== Reveal on Scroll (Intersection Observer) =====
const reveals = document.querySelectorAll('.reveal');

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry, idx) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, idx * 80);
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.08 }
);

reveals.forEach((el) => revealObserver.observe(el));

// ===== Navbar Scroll Effect =====
const nav = document.getElementById('main-nav');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const currentScroll = window.scrollY;
  if (currentScroll > 60) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
  lastScroll = currentScroll;
});

// ===== Mobile Navigation Toggle =====
const navToggle = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });

  // Close nav when a link is clicked
  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
    });
  });
}

// ===== Back to Top Button =====
const backToTop = document.getElementById('back-to-top');

if (backToTop) {
  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTop.classList.add('visible');
    } else {
      backToTop.classList.remove('visible');
    }
  });

  backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// ===== Active Nav Link Highlighting =====
const sections = document.querySelectorAll('section[id]');

const navHighlightObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        document.querySelectorAll('.nav-links a').forEach((link) => {
          link.style.color = '';
          link.style.background = '';
        });
        const activeLink = document.querySelector(`.nav-links a[href="#${id}"]`);
        if (activeLink && !activeLink.classList.contains('nav-cta')) {
          activeLink.style.color = '#22d3ee';
          activeLink.style.background = 'rgba(34, 211, 238, 0.08)';
        }
      }
    });
  },
  { threshold: 0.3, rootMargin: '-80px 0px -50% 0px' }
);

sections.forEach((section) => navHighlightObserver.observe(section));
