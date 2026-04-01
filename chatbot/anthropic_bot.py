import os
import streamlit as st
import anthropic
from dotenv import load_dotenv
from pathlib import Path

# Load API key from .env
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

api_key=os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

# --- Page Config ---
st.set_page_config(page_title="Claude Chatbot", page_icon="🤖")
st.title("🤖 Claude AI Chatbot")
st.caption("Powered by Anthropic Claude")

# --- System Prompt ---
SYSTEM_PROMPT = """
You are a helpful, friendly assistant.
Answer clearly and concisely.
"""

# --- Session State (keeps chat history) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display chat history ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Handle new user input ---
if prompt := st.chat_input("Ask me anything..."):

    # Add user message & display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Claude API with streaming
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            # Claude uses streaming natively — great for chatbots!
            full_reply = ""
            placeholder = st.empty()

            with client.messages.stream(
                model="claude-sonnet-4-5",   # smart & cost-effective
                max_tokens=1024,
                system=SYSTEM_PROMPT,        # note: Claude takes system separately
                messages=st.session_state.messages
            ) as stream:
                for text in stream.text_stream:
                    full_reply += text
                    placeholder.markdown(full_reply + "▌")  # live typing effect

            placeholder.markdown(full_reply)  # final clean render

    # Add assistant reply to history
    st.session_state.messages.append({"role": "assistant", "content": full_reply})