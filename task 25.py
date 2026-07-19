import streamlit as st
from backend import process_pdf, generate_rag_response

def init_session_state():
    """Initialize necessary session state variables for state management."""
    # Maintain the conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # Track whether a document has been successfully processed
    if "pdf_indexed" not in st.session_state:
        st.session_state.pdf_indexed = False

def clear_context():
    """Reset the document context and clear the chat history."""
    st.session_state.messages = []
    st.session_state.pdf_indexed = False

def render_sidebar():
    """Render the sidebar containing the document upload and management UI."""
    with st.sidebar:
        st.header("📄 Document Context")
        
        # PDF File Uploader
        uploaded_file = st.file_uploader(
            "Upload a PDF to chat with:", 
            type=["pdf"],
            help="Upload a document to provide a knowledge base for the chatbot."
        )
        
        # Process the newly uploaded PDF
        if uploaded_file is not None and not st.session_state.pdf_indexed:
            with st.spinner("Indexing document... Please wait."):
                try:
                    process_pdf(uploaded_file)
                    st.session_state.pdf_indexed = True
                    st.success("✅ Document indexed successfully!")
                except Exception as e:
                    st.error(f"Error processing the PDF: {e}")
                    
        # Persistent success state after upload
        elif st.session_state.pdf_indexed:
            st.success("✅ Active document context loaded.")
        
        st.divider()
        
        # Context management button
        if st.button("🗑️ Clear Document Context", use_container_width=True):
            clear_context()
            st.rerun()

def render_chat_interface():
    """Render the main chat interface and handle user interactions."""
    st.title("Interactive RAG Chatbot")
    
    # Render previous chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    # Handle new user input
    if prompt := st.chat_input("Ask a question about your document..."):
        
        # Enforce document dependency: User must upload a PDF first
        if not st.session_state.pdf_indexed:
            st.warning("⚠️ Please upload a PDF document from the sidebar before asking questions.")
            return

        # 1. Display and save the user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # 2. Generate, display, and save the assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = generate_rag_response(prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error generating a response from the backend: {e}")

def main():
    """Main execution block configuring the page and running the modules."""
    st.set_page_config(
        page_title="RAG Chatbot", 
        page_icon="🤖", 
        layout="wide"
    )
    
    init_session_state()
    render_sidebar()
    render_chat_interface()

if __name__ == "__main__":
    main()
