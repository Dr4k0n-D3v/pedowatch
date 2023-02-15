const toggleButton = document.querySelector("#sidebar-toggle-button");
const sidebar = document.querySelector("#sidebar");

toggleButton.addEventListener("click", function() {
  sidebar.classList.toggle("active");
});

document.getElementById("home-button").addEventListener("click", function() {
  window.location.href = "home.html";
});

const lbutton = document.getElementById("lbutton");
print(lbutton)
lbutton.addEventListener("click", function() {
  console.log('button clicked');
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  fetch('http://127.0.0.1:5000/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({email: email, password: password})
  })
  .then(response => {
    console.log('Success:', response);
    if (response.ok) {
      console.log('worked');
    } else {
      throw new Error('Server response was not OK');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
  console.log(JSON.stringify({email: email, password: password}));
});
