const chatBox = document.getElementById("chat-box");
const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});

function appendMessage(sender, text) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender);
    messageDiv.innerText = text;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    const text = userInput.value.trim();
    if (text === "") return;

    appendMessage("user", text);
    userInput.value = "";

    appendMessage("bot", "Typing...");

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    })
        .then(res => res.json())
        .then(data => {
            const typingMsg = chatBox.querySelector(".bot:last-child");
            typingMsg.remove();
            appendMessage("bot", data.reply);
        })
        .catch(err => console.error(err));
}
