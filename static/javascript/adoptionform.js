// Form Submission Handling
document.getElementById('adoptionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    // Perform additional validation or submission actions here
    
    // You can access form data using JavaScript and process it further
    const formData = new FormData(this);
    
    // For demonstration purposes, log the form data to the console
    for (const [key, value] of formData.entries()) {
      console.log(`${key}: ${value}`);
    }
    // You can send this data to a server or perform other actions as needed
    
    // Reset the form after submission (optional)
    this.reset();
  });
  