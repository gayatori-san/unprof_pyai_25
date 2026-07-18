import streamlit as st
# TODO: Import your RAG backend functions here
# from backend import process_pdf, generate_rag_response

# Configure the page
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="wide")

# --- INITIALIZE SESSION STATE ---
# This ensures data persists across app reruns (which happen on every click/input)
if "messages" not in st.session_state:
    st.session_state.messages = []
if "is_indexed" not in st.session_state:
    st.session_state.is_indexed = False

# --- DAY 26: SIDEBAR (PDF Upload & Auto-Indexing) ---
with st.sidebar:
    st.title("📄 Document Upload")
    st.markdown("Upload a PDF to contextually ground the chatbot.")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None and not st.session_state.is_indexed:
        with st.spinner("Extracting and indexing document..."):
            # TODO: Pass 'uploaded_file' to your backend vector database logic
            # process_pdf(uploaded_file)
            
            st.session_state.is_indexed = True
            st.success("PDF successfully indexed!")

    if st.session_state.is_indexed:
        st.info("✅ Document is loaded. The chatbot is ready to answer questions based on this file.")
        
        # Optional: Add a button to reset the context
        if st.button("Clear Document Context"):
            st.session_state.is_indexed = False
            st.session_state.messages = []
            st.rerun()

# --- DAY 25: MAIN CHAT INTERFACE ---
st.title("💬 Interactive RAG Chatbot")

# Render existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user query
if prompt := st.chat_input("Ask a question about your uploaded document..."):
    
    # 1. Display user message and add to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Generate and display AI response
    with st.chat_message("assistant"):
        if not st.session_state.is_indexed:
            response = "Please upload and index a PDF from the sidebar first so I have context!"
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            with st.spinner("Searching document..."):
                # TODO: Pass the 'prompt' to your backend RAG generation function
                # response = generate_rag_response(prompt)
                
                # Placeholder response until you connect the backend:
                response = f"This is a placeholder answer to: **'{prompt}'**. Plug in your RAG backend to see real answers!"
                
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})