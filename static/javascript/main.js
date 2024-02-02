// main.js

document.addEventListener('DOMContentLoaded', () => {
  // Login form submission
  document.getElementById('login').addEventListener('login in', (event) => {
      event.preventDefault(); // Prevent default form submission
      const username = document.getElementById('loginUsername').value;
      const password = document.getElementById('loginPassword').value;

      // Perform login authentication (You will need to send this data to your server)
      // Example using fetch API to make a POST request to your backend
      fetch('/login', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password }),
      })
      .then(response => {
          // Handle response, e.g., check for successful login status
          if (response.ok) {
              // Redirect to the dashboard or perform other actions on successful login
              window.location.href = '/dash'; // Redirect to dashboard page
          } else {
              // Handle login failure, display error messages, etc.
              console.error('Login failed');
          }
      })
      .catch(error => {
          console.error('Error:', error);
      });
  });

  // Signup form submission
  document.getElementById('signup').addEventListener('signup', (event) => {
      event.preventDefault(); // Prevent default form submission
      const username = document.getElementById('signupemail').value;
      const password = document.getElementById('signupPassword').value;

      // Perform signup (You will need to send this data to your server)
      // Example using fetch API to make a POST request to your backend
      fetch('/signup', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password }),
      })
      .then(response => {
          // Handle response, e.g., check for successful signup status
          if (response.ok) {
              // Redirect to the dashboard or perform other actions on successful signup
              window.location.href = '/dash'; // Redirect to dashboard page
          } else {
              // Handle signup failure, display error messages, etc.
              console.error('Signup failed');
          }
      })
      .catch(error => {
          console.error('Error:', error);
      });
  });
});
