# app.py
import streamlit as st
from mvp.mvp_pipeline import SummarizationPipeline
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Text Summarizer & Paraphraser",
    page_icon="📝",
    layout="wide"
)

# Get API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    st.error("⚠️ Hugging Face API key not found! Please add HF_API_KEY to your .env file")
    st.info("Get your API key from: https://huggingface.co/settings/tokens")
    st.stop()

if not GROQ_API_KEY:
    st.warning("⚠️ Groq API key not found! Paraphrasing may not work until you add GROQ_API_KEY to your .env file.")

# Initialize pipeline
@st.cache_resource
def load_pipeline():
    return SummarizationPipeline(HF_API_KEY)

try:
    pipeline = load_pipeline()
except Exception as e:
    st.error(f"Failed to initialize pipeline: {str(e)}")
    st.stop()

# Header
st.title("📝 AI Text Summarizer & Paraphraser")
st.markdown("🚀 **Powered by Hugging Face & Groq API** - No model downloads required!")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    method = st.radio(
        "Summarization Method",
        ["Extractive", "Abstractive"],
        help="Extractive: Selects important sentences. Abstractive: Generates new summary."
    )
    
    length = st.select_slider(
        "Summary Length",
        options=["Short", "Medium", "Long"],
        value="Medium"
    )
    
    st.markdown("---")
    st.markdown("### 🔐 API Status")
    if HF_API_KEY:
        st.success("✓ Hugging Face API Key Loaded")
        st.caption(f"{HF_API_KEY[:8]}...{HF_API_KEY[-4:]}")
    if GROQ_API_KEY:
        st.success("✓ Groq API Key Loaded")
        st.caption(f"{GROQ_API_KEY[:8]}...{GROQ_API_KEY[-4:]}")

# Main content
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Input Text")
    input_text = st.text_area(
        "Paste your text here",
        height=300,
        placeholder="Enter the text you want to summarize or paraphrase..."
    )
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        summarize_btn = st.button("✨ Summarize", use_container_width=True, type="primary")
    with col_btn2:
        paraphrase_btn = st.button("🔄 Paraphrase", use_container_width=True)

with col2:
    st.subheader("📊 Output")
    
    if summarize_btn and input_text:
        with st.spinner("🔄 Calling Hugging Face API..."):
            try:
                summary = pipeline.summarize(
                    input_text,
                    method=method.lower(),
                    length=length.lower()
                )
                
                if summary.startswith("Error") or summary.startswith("API Error"):
                    st.error(summary)
                else:
                    st.success("✅ Summary Generated!")
                    st.text_area("Summary", summary, height=300, key="summary_output")
                    
                    # Download button
                    st.download_button(
                        label="⬇️ Download Summary",
                        data=summary,
                        file_name="summary.txt",
                        mime="text/plain"
                    )
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    elif paraphrase_btn and input_text:
        with st.spinner("🔄 Calling Groq API..."):
            try:
                paraphrases = pipeline.paraphrase(input_text)
                
                if paraphrases and isinstance(paraphrases, list):
                    st.success(f"✅ {len(paraphrases)} Paraphrases Generated!")
                    for i, p in enumerate(paraphrases, 1):
                        st.text_area(f"Paraphrase {i}", p, height=150, key=f"paraphrase_{i}")
                        
                        # Download button
                        st.download_button(
                            label=f"⬇️ Download Paraphrase {i}",
                            data=p,
                            file_name=f"paraphrase_{i}.txt",
                            mime="text/plain"
                        )
                else:
                    st.error("No paraphrases generated.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    elif not input_text:
        st.info("👈 Enter some text and click a button to get started!")
        
        # Show features
        st.markdown("### 🌟 Features")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            ✓ API-based processing  
            ✓ No model downloads  
            ✓ Fast cloud inference  
            """)
        with col_b:
            st.markdown("""
            ✓ Secure API keys  
            ✓ Multiple models  
            ✓ Real-time results  
            """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Built with Streamlit • Powered by Hugging Face & Groq API • No Local Models Required"
    "</div>",
    unsafe_allow_html=True
)
