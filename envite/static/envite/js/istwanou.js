// /* Scroll observer — combined */
// const observer = new IntersectionObserver((entries) => {
//     entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
// }, { threshold: 0 });

// /* Observe toc container */
// const toc = document.querySelector('.toc-container');
// if (toc) observer.observe(toc);

// /* Observe each toc-link */
// const links = document.querySelectorAll('.toc-link');
// links.forEach(link => observer.observe(link));

/* Scroll observer */
const toc = document.querySelector('.toc-container');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.15 });

if (toc) observer.observe(toc);

/* Scroll observer */
const links = document.querySelectorAll('.toc-link');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1 });

links.forEach(link => observer.observe(link));