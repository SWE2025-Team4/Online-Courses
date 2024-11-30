
const stars = document.querySelectorAll('.star');
const reviews = document.querySelector('.review');

stars.forEach((star, index) => {
    star.addEventListener('mouseover', () => {
        stars.forEach((s, i) => {
            s.style.color = i <= index ? 'gold' : '#ccc';
        });
    });

    star.addEventListener('click', () => {
        reviews.textContent = `(${index + 1} Review${index > 0 ? 's' : ''})`;
    });

    star.addEventListener('mouseout', () => {
        stars.forEach((s) => {
            s.style.color = s.classList.contains('empty') ? '#ccc' : 'gold';
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const layers = document.querySelectorAll('.layer-up-1, .layer-up-2, .layer-down-1, .layer-down-2');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            } else {
                entry.target.classList.remove('animate'); // Optional: Remove class if you want to reset
            }
        });
    }, {
        threshold: 0.1 // Trigger when 10% of the element is visible
    });

    layers.forEach(layer => observer.observe(layer));
});


