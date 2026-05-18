# CLI AI Chatbot with Persistent Memory

A powerful Command Line Interface (CLI) AI chatbot built using Python and the Groq API.  
This chatbot supports:

- Conversational AI
- Persistent memory using JSON
- Multi-turn conversations
- OpenAI-compatible architecture
- Environment variable security
- Groq LLM integration

---

# Features

## AI Chatbot
Uses Groq's OpenAI-compatible API to generate responses.

## Persistent Memory
The chatbot remembers previous conversations even after restarting the program.

## Multi-turn Conversations
Conversation history is continuously stored and sent to the AI model.

## Beginner-Friendly Architecture
Simple and modular structure for learning conversational AI systems.

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Groq API | AI model inference |
| OpenAI SDK | API communication |
| python-dotenv | Environment variable handling |
| JSON | Persistent memory storage |

---

# Project Structure

```text
chatbot/
│
├── main.py
├── memory.json
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-repository-link>
cd chatbot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Setup API Key

## Create a `.env` File

Inside your project folder, create:

```text
.env
```

Add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

---

# Getting a Groq API Key

1. Visit the Groq Console
2. Create an account
3. Generate an API key
4. Copy the key into your `.env` file

Groq Console:
https://console.groq.com/

---

# Running the Chatbot

```bash
python main.py
```

---

# Example Usage

```text
Chat Started...
Type 'exit' to end the conversation.

You: Hello
Assistant: Hi! How can I help you today?

You: My name is Aditya
Assistant: Nice to meet you, Aditya!

You: What is my name?
Assistant: Your name is Aditya.
```

---

# How Persistent Memory Works

The chatbot stores conversation history inside:

```text
memory.json
```

Every message is:
1. Added to conversation memory
2. Sent to the AI model
3. Saved permanently in JSON format

This allows the chatbot to remember previous conversations after restarting.

---

# Core Concepts Used

## System Messages
Define chatbot behavior and personality.

Example:

```python
{
    "role": "system",
    "content": "You are a helpful assistant."
}
```

---

## User Messages
Represent user input.

Example:

```python
{
    "role": "user",
    "content": "Hello"
}
```

---

## Assistant Messages
Store AI responses.

Example:

```python
{
    "role": "assistant",
    "content": "Hi!"
}
```

---

# Future Improvements

Possible upgrades for the project:

- Streaming responses
- Semantic memory
- SQLite database
- Vector databases
- Voice assistant integration
- Tool usage (web search, calculator, files)
- GUI interface
- Multi-agent architecture

---

# Resume Value

This project demonstrates:

- Python programming
- API integration
- Conversational AI systems
- Context management
- Persistent storage
- Environment variable security
- LLM application development

---

# Requirements

```text
openai
python-dotenv
```

---

# License

This project is open-source and available for educational purposes.

---

# Author

Built by Aditya Jhinjha
