const menuIcon = document.querySelector(".menu");
const menuList = document.querySelector(".nav-list");

menuIcon.addEventListener("click", () => {
  menuIcon.classList.toggle("menu-active");
  menuList.classList.toggle("nav-list_active");
});

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
  if (window.scrollY > 100) {
    navbar.classList.add("fixed");
  } else {
    navbar.classList.remove("fixed");
  }
});



