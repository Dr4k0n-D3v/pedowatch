const toggleButton = document.querySelector("#sidebar-toggle-button");
const sidebar = document.querySelector("#sidebar");

toggleButton.addEventListener("click", function() {
  sidebar.classList.toggle("active");
});

document.getElementById("home-button").addEventListener("click", function() {
  window.location.href = "home.html";
});

const loginButton = document.getElementById("login-button");
console.log(loginButton);

const lButton = document.getElementById("lbutton");
lButton.addEventListener("click", function() {
  console.log('button clicked');
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  fetch('http://127.0.0.1:5000/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: {'email': 'myusername', 'password': 'mypassword'}
  })
    .then(res => {
      return res.json();
    })
    .then(data => {
      console.log(data);
    })
    .catch(err => {
      console.error(err);
    });
    console.log('button clicked');
});