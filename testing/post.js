const toggleButton = document.querySelector("#sidebar-toggle-button");
const sidebar = document.querySelector("#sidebar");

toggleButton.addEventListener("click", function() {
  sidebar.classList.toggle("active");
});

document.getElementById("home-button").addEventListener("click", function() {
  window.location.href = "home.html";
});