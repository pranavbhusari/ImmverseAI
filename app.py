"""
Multilingual QnA Generation System using Streamlit
"""
import streamlit as st
import os
import tempfile
from datetime import datetime
from dotenv import load_dotenv
from document_parser import DocumentParser
from qna_generator import QnAGenerator
from translator import LanguageTranslator
from excel_exporter import ExcelExporter
from typing import List, Dict, Optional

# Load environment variables from .env file
load_dotenv()


# Configure page
st.set_page_config(
    page_title="Multilingual QnA Generator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        background-color: #d4edda;
        border-radius: 0.5rem;
        color: #155724;
    }
    .info-box {
        padding: 1rem;
        background-color: #d1ecf1;
        border-radius: 0.5rem;
        color: #0c5460;
    }
    .error-box {
        padding: 1rem;
        background-color: #f8d7da;
        border-radius: 0.5rem;
        color: #721c24;
    }
    </style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables"""
    if 'document_text' not in st.session_state:
        st.session_state.document_text = None
    if 'qna_pairs' not in st.session_state:
        st.session_state.qna_pairs = None
    if 'processing_status' not in st.session_state:
        st.session_state.processing_status = None


def upload_document() -> Optional[str]:
    """Handle document upload and parsing"""
    st.subheader("📄 Step 1: Upload Document")
    
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['pdf', 'docx', 'txt'],
        help="Supported formats: PDF, DOCX, TXT"
    )
    
    if uploaded_file is not None:
        with st.spinner("Processing document..."):
            try:
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                    tmp_file.write(uploaded_file.getbuffer())
                    tmp_file_path = tmp_file.name
                
                # Parse document
                parser = DocumentParser()
                document_text = parser.parse_document(tmp_file_path)
                
                # Clean up
                os.unlink(tmp_file_path)
                
                if document_text.strip():
                    st.session_state.document_text = document_text
                    st.success(f"✅ Document uploaded successfully! ({len(document_text)} characters)")
                    
                    # Show document preview
                    with st.expander("📋 Document Preview"):
                        st.text_area(
                            "Document Content Preview",
                            value=document_text[:1000] + "..." if len(document_text) > 1000 else document_text,
                            height=200,
                            disabled=True
                        )
                else:
                    st.error("❌ Could not extract text from document")
            
            except Exception as e:
                st.error(f"❌ Error processing document: {str(e)}")
    
    return st.session_state.document_text


def configure_qna_generation() -> tuple:
    """Configure QnA generation parameters"""
    st.subheader("⚙️ Step 2: Configure QnA Generation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_questions = st.slider(
            "Number of QnA pairs per chunk",
            min_value=1,
            max_value=10,
            value=3,
            help="More questions = more detailed output"
        )
    
    with col2:
        chunk_size = st.slider(
            "Text chunk size",
            min_value=500,
            max_value=2000,
            value=1000,
            help="Size of text chunks for processing"
        )
    
    # Get API key from environment
    env_api_key = os.getenv('GROQ_API_KEY')
    
    if env_api_key:
        st.success("✅ Groq API Key loaded from .env file")
        api_key = env_api_key
    else:
        api_key = st.text_input(
            "Groq API Key (Required)",
            type="password",
            help="Get your free API key from https://console.groq.com (10,000 requests/day free!)"
        )
    
    return num_questions, chunk_size, api_key


def generate_qna(document_text: str, num_questions: int, chunk_size: int, api_key: str) -> Optional[List[Dict[str, str]]]:
    """Generate QnA pairs from document text"""
    st.subheader("🔄 Step 3: Generate QnA Pairs")
    
    if st.button("🚀 Generate QnA Pairs", key="generate_btn"):
        try:
            # Set API key
            os.environ['GOOGLE_API_KEY'] = api_key
            
            with st.spinner("Generating QnA pairs from entire document..."):
                # IMPORTANT: Process ENTIRE document as ONE request (not per chunk)
                # This respects the 20 requests/day free tier quota
                parser = DocumentParser()
                chunks = parser.chunk_text(document_text, chunk_size=chunk_size)
                
                st.info(f"📊 Processing entire document as single API request")
                st.info(f"   (Document contains ~{len(chunks)} logical sections)")
                
                # Generate QnA pairs - pass chunks to combine into one request
                generator = QnAGenerator(api_key)
                
                with st.spinner("Calling Google Gemini API..."):
                    try:
                        # generate_qna_batch combines all chunks and makes ONE API call
                        all_qna = generator.generate_qna_batch(chunks, num_questions_per_chunk=num_questions)
                    except Exception as e:
                        st.error(f"❌ Error generating QnA: {str(e)}")
                        return None
                
                st.session_state.qna_pairs = all_qna
                st.success(f"✅ Generated {len(all_qna)} QnA pairs!")
                
                # Display generated QnA
                st.subheader("Generated QnA Pairs (English)")
                for idx, qna in enumerate(all_qna[:5], 1):  # Show first 5
                    with st.expander(f"Q{idx}: {qna['question'][:50]}..."):
                        st.write(f"**Question:** {qna['question']}")
                        st.write(f"**Answer:** {qna['answer']}")
                
                if len(all_qna) > 5:
                    st.info(f"Showing 5 of {len(all_qna)} pairs. All pairs will be included in the export.")
        
        except Exception as e:
            st.error(f"❌ Error generating QnA: {str(e)}")
            return None
    
    return st.session_state.qna_pairs


def translate_and_export(qna_pairs: List[Dict[str, str]]) -> Optional[str]:
    """Translate QnA pairs and create Excel file"""
    st.subheader("🌐 Step 4: Translate & Export")
    
    if st.button("🔄 Translate to Hindi and Marathi", key="translate_btn"):
        try:
            with st.spinner("Translating QnA pairs..."):
                translator = LanguageTranslator()
                
                # Translate to Hindi
                st.info("Translating to Hindi...")
                hindi_qna = translator.translate_qna_pairs(qna_pairs, 'hi')
                
                # Translate to Marathi
                st.info("Translating to Marathi...")
                marathi_qna = translator.translate_qna_pairs(qna_pairs, 'mr')
                
                st.success("✅ Translation complete!")
                
                # Create Excel file
                with st.spinner("Creating Excel file..."):
                    exporter = ExcelExporter()
                    output_path = exporter.create_multilingual_qna_file(
                        english_qna=qna_pairs,
                        hindi_qna=hindi_qna,
                        marathi_qna=marathi_qna
                    )
                
                st.success(f"✅ Excel file created: {output_path}")
                
                # Provide download button
                with open(output_path, 'rb') as file:
                    st.download_button(
                        label="📥 Download Multilingual_QnA.xlsx",
                        data=file.read(),
                        file_name="Multilingual_QnA.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                
                return output_path
        
        except Exception as e:
            st.error(f"❌ Error during translation/export: {str(e)}")
            return None


def main():
    """Main Streamlit application"""
    initialize_session_state()
    
    # Header
    st.markdown("""
        <div class="header">
            <h1>🌍 Multilingual QnA Generator</h1>
            <p>Automatically generate Question-Answer pairs in English, Hindi, and Marathi</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar instructions
    with st.sidebar:
        st.markdown("### 📖 Instructions")
        st.markdown("""
        1. **Upload Document**: Choose a PDF, DOCX, or TXT file
        2. **Configure Settings**: Set QnA generation parameters
        3. **Generate QnA**: Create question-answer pairs from content
        4. **Translate & Export**: Generate multilingual Excel output
        
        ### 🔑 Groq API Key Setup
        Your API key is loaded from the `.env` file.
        
        To change it, edit `.env`:
        ```
        GROQ_API_KEY=your_key_here
        ```
        
        Get your free API key from:
        https://console.groq.com
        
        ### ⚡ Free Tier Quota
        - **10,000 requests per day** (vs Gemini's 20!)
        - Excellent quality with Mixtral model
        - No credit card required
        - Perfect for development
        
        ### 📋 Supported Formats
        - PDF, DOCX, TXT
        
        ### ⭐ Features
        - Powered by **Groq API** (Free 10k/day!)
        - Using **Mixtral-8x7b** model
        - Multi-language support (English, Hindi, Marathi)
        - Excel export with formatted sheets
        - Can process up to 5 chunks per document
        """)
    
    # Check for API key in environment
    env_api_key = os.getenv('GROQ_API_KEY')
    if env_api_key:
        st.success("✅ Groq API Key loaded from .env file")
    else:
        st.warning("⚠️ Groq API Key not found in .env file")
    
    # Main workflow
    document_text = upload_document()
    
    if document_text:
        num_questions, chunk_size, api_key = configure_qna_generation()
        
        if not api_key or api_key.strip() == "":
            st.error("❌ Please provide your Google API Key to proceed")
        else:
            qna_pairs = generate_qna(document_text, num_questions, chunk_size, api_key)
            
            if qna_pairs:
                translate_and_export(qna_pairs)
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: gray;">
            <small>Multilingual QnA Generation System | Built with Streamlit</small>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
