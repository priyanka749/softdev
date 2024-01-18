
document.addEventListener('DOMContentLoaded', function () {
  var alertElement = document.getElementById('alert-1');
  var closeButton = alertElement.querySelector('[data-dismiss-target="#alert-1"]');
  var emailInput = document.getElementById("email");
  var passwordInput = document.getElementById("pass1"); // Assuming 'pass1' is the correct ID for the password input field
  const rememberMeCheckbox = document.getElementById("remember");

  // Load stored "Remember Me" data from local storage
  const storedData = localStorage.getItem("rememberMeData");
  if (storedData) {
      const data = JSON.parse(storedData);
      emailInput.value = data.email; // Fixed variable name for email input
      passwordInput.value = data.password;
      rememberMeCheckbox.checked = true;
  }

  // Check if "Remember Me" is checked and save data to local storage
  rememberMeCheckbox.addEventListener('change', function () {
      if (rememberMeCheckbox.checked) {
          const rememberMeData = JSON.stringify({ email: emailInput.value, password: passwordInput.value });
          localStorage.setItem("rememberMeData", rememberMeData);
      } else {
          localStorage.removeItem("rememberMeData");
      }
  });

  // Close the alert when the close button is clicked
  closeButton.addEventListener('click', function () {
      alertElement.style.display = 'none';
  });

  // Fade away the alert after 5 seconds if the user does not click the close button
  setTimeout(function () {
      alertElement.style.transition = 'opacity 1s ease-out';
      alertElement.style.opacity = 0;
      setTimeout(function () {
          alertElement.style.display = 'none';
      }, 1000);
  }, 5000);
});

function togglePassword() {
  var passwordField = document.getElementById("pass1");
  var eyeIcon = document.getElementById("eyeIcon");

  if (passwordField.type === "password") {
      passwordField.type = "text";
      eyeIcon.classList.remove("fa-eye");
      eyeIcon.classList.add("fa-eye-slash");
  } else {
      passwordField.type = "password";
      eyeIcon.classList.remove("fa-eye-slash");
      eyeIcon.classList.add("fa-eye");
  }
}
