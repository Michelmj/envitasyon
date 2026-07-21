
/* Scroll observer */
const sections = document.querySelectorAll('.section');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.15 });
sections.forEach(s => observer.observe(s));

/* Parking Spot */
const parkingImg = document.querySelector('.parking-img');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');

parkingImg.addEventListener('click', () => {
    lightboxImg.src = parkingImg.src;
    lightbox.classList.add('active');
});

let scale = 1;

lightbox.addEventListener('click', () => {
    lightbox.classList.remove('active');
      scale = 1;
    lightboxImg.style.transform = 'scale(1)';
});

lightboxImg.addEventListener('wheel', (e) => {
    e.preventDefault();
    scale += e.deltaY * -0.01;
    scale = Math.min(Math.max(1, scale), 4); // min 1x, max 4x
    lightboxImg.style.transform = `scale(${scale})`;
});

