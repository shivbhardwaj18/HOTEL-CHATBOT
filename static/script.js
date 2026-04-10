function addMessage(text, className) {
    const chat = document.getElementById("chat");

    const msg = document.createElement("div");
    msg.className = "message " + className;

    msg.innerText = text;

    chat.appendChild(msg);
    chat.scrollTop = chat.scrollHeight;
}
window.onload = function() {
    addMessage("Hello! How can I assist you today?", "bot");
};

function sendMessage() {
    const input = document.getElementById("input");
    const text = input.value.trim();

    if (!text) return;

    addMessage(text, "user");
    input.value = "";

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: text })
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.response, "bot");
    });
}

function handleKey(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}
