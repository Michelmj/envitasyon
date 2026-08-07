/* Scroll observer — combined */
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1 });

/* Observe toc container */
const toc = document.querySelector('.toc-container');
if (toc) observer.observe(toc);

/* Observe each toc-link */
const links = document.querySelectorAll('.toc-link');
links.forEach(link => observer.observe(link));