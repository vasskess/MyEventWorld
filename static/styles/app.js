const toggleBtn = document.getElementsByClassName("nav-toggle")[0];
const links = document.getElementsByClassName("nav-links")[0];

toggleBtn.addEventListener("click", navToggle);

function navToggle() {
    links.classList.toggle("show-links");
}

window.addEventListener('DOMContentLoaded', function () {
    window.addEventListener('scroll', function () {
        const footer = document.getElementsByClassName('footer')[0];
        const scrollPosition = window.scrollY;

        const documentHeight = document.documentElement.scrollHeight;
        const viewportHeight = window.innerHeight;

        if (scrollPosition + viewportHeight >= documentHeight) {
            footer.style.display = 'flex';
        } else {
            footer.style.display = 'none';
        }
    });
});