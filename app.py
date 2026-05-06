import streamlit as st
from chatbot import chat_with_bot

st.set_page_config(page_title="Local LangChain Chatbot")

st.title("🤖 Local LangChain Chatbot (No API Key)")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response
    response = chat_with_bot(user_input)

    # Show bot response
    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
