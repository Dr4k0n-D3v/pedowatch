const toggleButton = document.querySelector("#sidebar-toggle-button");
const sidebar = document.querySelector("#sidebar");

toggleButton.addEventListener("click", function() {
  sidebar.classList.toggle("active");
});

document.getElementById("post-button").addEventListener("click", function() {
  window.location.href = "post.html";
});

document.getElementById("login-button").addEventListener("click", function() {
  window.location.href = "login.html";
});