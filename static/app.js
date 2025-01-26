function sendMessage() {
    const inputField = document.getElementById("userInput");
    const message = inputField.value.trim();
    if (!message) return;
  
    // Display the user's message
    const messagesDiv = document.getElementById("messages");
    const userMessage = document.createElement("div");
    userMessage.textContent = "You: " + message;
    messagesDiv.appendChild(userMessage);
  
    // Send message to server
    fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Display bot response
        const botMessage = document.createElement("div");
        botMessage.textContent = "Bot: " + data.response;
        messagesDiv.appendChild(botMessage);
        messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll
      });
  
    // Clear input field
    inputField.value = "";
  }