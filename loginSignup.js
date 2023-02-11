let signupData = [];

fetch('http://localhost:8080/signupData.json')
  .then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Failed to fetch signupData.json');
  })
  .then(data => {
    signupData = data;
  })
  .catch(error => {
    console.error(error);
  });

document.getElementById('signupForm').addEventListener('submit', function(event) {
  event.preventDefault();

  let name = document.getElementById('name').value;
  let email = document.getElementById('email').value;
  let password = document.getElementById('password').value;

  signupData.push({ name, email, password });

  fetch('http://localhost:8080/signupData.json', {
    method: 'PUT',
    body: JSON.stringify(signupData),
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(response => {
      if (response.ok) {
        console.log('Sign up data saved successfully');
      } 
      else {
        throw new Error('Failed to save sign up data');
      }
    })
    .catch(error => {
      console.error(error);
    });
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault();

  let email = document.getElementById('email').value;
  let password = document.getElementById('password').value;

  let user = signupData.find(user => user.email === email && user.password === password);

  if (user) {
    alert('Login successful!');
  } 
  else {
    alert('Login failed. Please try again.');
  }
});