# 🤖 Claude AI Chatbot

A conversational AI chatbot built with Anthropic's Claude API and Streamlit, featuring real-time streaming responses and multi-turn chat memory.

---

## 🚀 Features

- 💬 Multi-turn conversation with chat history
- ⚡ Real-time streaming responses with live typing effect
- 🔒 Secure API key management with environment variables
- 🎨 Clean, responsive web UI powered by Streamlit

---

## 🛠️ Tech Stack

- **[Anthropic Claude API](https://www.anthropic.com/)** — AI language model
- **[Streamlit](https://streamlit.io/)** — Web interface
- **Python 3.11**

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/SushilDhadse/claude-chatbot.git
cd claude-chatbot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install anthropic streamlit python-dotenv
```

### 4. Set up your API key
Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your-api-key-here
```
Get your API key from [console.anthropic.com](https://console.anthropic.com)

### 5. Run the app
```bash
streamlit run chatbot/anthropic_bot.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📁 Project Structure

```
claude-chatbot/
├── chatbot/
│   └── anthropic_bot.py   # Main chatbot application
├── .env                   # API key (never commit this!)
├── .gitignore             # Protects .env from being pushed
└── README.md
```

---

## 🔒 Security

This project uses a `.env` file to store the API key securely.
The `.gitignore` ensures it is never committed to version control.

---

## 📌 Future Improvements

- [ ] Add RAG (Retrieval-Augmented Generation) pipeline
- [ ] Connect to Snowflake for data storage
- [ ] Add document upload and Q&A functionality
- [ ] Deploy to cloud (AWS / Azure)

---

## 👤 Author

**Sushil Dhadse**  
[GitHub](https://github.com/SushilDhadse)
