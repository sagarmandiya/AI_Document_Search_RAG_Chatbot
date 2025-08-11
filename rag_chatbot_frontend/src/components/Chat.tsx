// src/components/Chat.tsx

import React, { useState } from "react";
import { askQuestion, ChatResponse } from "../api/chatbot";

const Chat: React.FC = () => {
  const [input, setInput] = useState<string>("");
  const [chatLog, setChatLog] = useState<Array<{ role: "user" | "bot"; text: string }>>([]);

  const handleSend = async () => {
    if (!input.trim()) return;
    const userMsg = input.trim();
    setChatLog((log) => [...log, { role: "user", text: userMsg }]);
    setInput("");

    try {
      const { answer } = await askQuestion(userMsg);
      setChatLog((log) => [...log, { role: "bot", text: answer }]);
    } catch (error) {
      setChatLog((log) => [...log, { role: "bot", text: "Error: Unable to get response." }]);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 16 }}>
      <h2>RAG Chatbot</h2>
      <div style={{ height: 400, overflowY: "auto", border: "1px solid #ccc", padding: 8, marginBottom: 8 }}>
        {chatLog.map((entry, idx) => (
          <div key={idx} style={{ margin: "8px 0" }}>
            <b>{entry.role === "user" ? "You" : "Bot"}:</b> {entry.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
        placeholder="Ask your question..."
        style={{ width: "80%", padding: 8 }}
      />
      <button onClick={handleSend} style={{ padding: 8, marginLeft: 8 }}>
        Send
      </button>
    </div>
  );
};

export default Chat;
