import streamlit as st
from chatbot import chat_with_bot

st.set_page_config(page_title="Local LangChain Chatbot")

st.title("🤖 Local LangChain Chatbot (No API Key)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = chat_with_bot(user_input)

    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
