// src/api/chatbot.ts
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000"; // Replace with your deployed backend URL

export interface ChatResponse {
  answer: string;
}

export async function askQuestion(question: string): Promise<ChatResponse> {
  const response = await axios.post(`${API_BASE_URL}/ask`, { question });
  return response.data;
}
