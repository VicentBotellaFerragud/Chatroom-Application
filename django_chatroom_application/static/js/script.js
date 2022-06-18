let messageInput = document.getElementById('messageInput');

messageInput.addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
      // Cancel the default action, if needed
      event.preventDefault();
      // Trigger the button element with a click
      triggerAlert();
    }
  });

function triggerAlert() {
    if (messageInput.value === '') {
        alert("Please type a message before clicking the 'SEND' button");
    }
}