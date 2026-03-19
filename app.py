import os
import streamlit as st
from logic import document_processing, agent

# Step 1: Set Page Configuraton
st.set_page_config(page_title="Simple RAG Agent", page_icon="🤖")
st.title("🤖 PDF Supported RAG Agent")
st.markdown("________")

document_path = "./logic/ultimate-guide-to-digital-marketing.pdf"
vector_db_path = "./logic/vector_db_rag_tutorial"

# Step 2: Set Cache to ensures the document is only processed ONCE, even if 10 people use the site.
@st.cache_resource
def initialize_system():
    # if not os.path.exists(vector_db_path):
        with st.status("Intitializing Vector Database"):
            try:
                document_processing.process_document_for_rag(file_path=document_path)
                st.write("Initialization successful!")
            except Exception as e:
                print("Initialization of doument is failed. ", e)
                st.stop()
    # return True

system_ready = initialize_system()

# Step 3: create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Step 4: Main chain input
if user_query := st.chat_input("What's in your mind about AI Agents today?"):

    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)
    
    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            try:
                # Get response from your agent logic
                response = agent.ask_agent(user_query)
                st.markdown(response)
                
                # Save assistant response to state
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Step 5. Sidebar for Demo Flair 
with st.sidebar:
    st.header("Project Info")
    st.write("📌 **Source:** Beginners Guide to AI Agents")
    st.write("📂 **Status:** Vector DB Linked")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()




