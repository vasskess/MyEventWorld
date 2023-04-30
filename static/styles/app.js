const toggleBtn = document.getElementsByClassName("nav-toggle")[0];
const links = document.getElementsByClassName("nav-links")[0];

toggleBtn.addEventListener("click", navToggle);

function navToggle() {
  links.classList.toggle("show-links");
}