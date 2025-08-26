from model import chat # Import the chat function from models.py
import streamlit as st 

# Set page config
st.set_page_config(
    page_title="Chat App",
    page_icon="💬",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# App title
st.title("💬 Chat App")
st.markdown("Chat with the AI model from models.py")

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get response from the model
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Call the chat function from models.py
                response = chat(prompt)
                st.markdown(response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Sidebar with chat controls
with st.sidebar:
    st.header("Chat Controls")
    
    if st.button("Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown(f"**Messages:** {len(st.session_state.messages)}")
    
    # Optional: Export chat history
    if st.session_state.messages:
        if st.button("Export Chat"):
            chat_export = ""
            for msg in st.session_state.messages:
                chat_export += f"**{msg['role'].title()}:** {msg['content']}\n\n"
            st.download_button(
                label="Download Chat History",
                data=chat_export,
                file_name="chat_history.txt",
                mime="text/plain"
            )