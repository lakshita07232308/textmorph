# app.py
import streamlit as st
from config_manager import ConfigManager
from mvp.mvp_pipeline import SummarizationPipeline
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
cfg = ConfigManager()

HF_API_KEY = os.getenv(cfg.get("api_keys", "huggingface"))
GROQ_API_KEY = os.getenv(cfg.get("api_keys", "groq"))

# Streamlit Page Config
st.set_page_config(page_title="TextMorph ", page_icon="|", layout="wide")

# 🌈 Custom CSS Styling (Glassmorphism Theme)
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }

    .main {
        background: linear-gradient(135deg, #ffffffaa, #f0f0f0aa);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    }

    h1 {
        text-align: center;
        font-size: 2.2em;
        background: -webkit-linear-gradient(#0078ff, #00c6ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .stButton>button {
        border-radius: 12px;
        height: 3em;
        background: linear-gradient(90deg, #0078ff, #00c6ff);
        color: white;
        border: none;
        font-weight: 600;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #00c6ff, #0078ff);
    }

    .stTextArea textarea {
        background-color: #f8fafc;
        border-radius: 10px;
        border: 1px solid #d0d7de;
        font-size: 1rem;
        padding: 10px;
    }

    .css-1d391kg p {
        font-size: 1.1rem;
    }

    .output-box {
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
        padding: 15px;
        margin-top: 10px;
    }

    .footer {
        text-align: center;
        color: #888;
        font-size: 0.9rem;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Load the pipeline
@st.cache_resource
def load_pipeline():
    return SummarizationPipeline(HF_API_KEY, cfg)

pipeline = load_pipeline()

# Title
st.title("📝 TextMorph")
st.markdown("### 🚀 AI Text Summarizer & Paraphraser (Hugging Face + Groq API)")

st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    method = st.radio("Summarization Method", ["Extractive", "Abstractive"])
    length = st.select_slider("Summary Length", ["Short", "Medium", "Long"], value="Medium")
    st.markdown("---")
    st.markdown("### 🔐 API Keys Status")
    st.success("✓ Hugging Face Key Loaded" if HF_API_KEY else "⚠️ Missing HF_API_KEY")
    st.success("✓ Groq Key Loaded" if GROQ_API_KEY else "⚠️ Missing GROQ_API_KEY")

# Main layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📄 Input Text")
    input_text = st.text_area("Paste your text here", height=280, placeholder="Enter your content...")

    col_a, col_b = st.columns(2)
    with col_a:
        summarize_btn = st.button("✨ Summarize", use_container_width=True)
    with col_b:
        paraphrase_btn = st.button("🔄 Paraphrase", use_container_width=True)

with col2:
    st.subheader("📊 Output")

    if summarize_btn and input_text.strip():
        with st.spinner("⚙️ Generating summary via Hugging Face..."):
            summary = pipeline.summarize(input_text, method=method.lower(), length=length.lower())
            st.markdown("#### ✅ Summary Result")
            st.markdown(f"<div class='output-box'>{summary}</div>", unsafe_allow_html=True)
            st.download_button("⬇️ Download Summary", summary, "summary.txt")

    elif paraphrase_btn and input_text.strip():
        with st.spinner("⚙️ Generating paraphrases via Groq..."):
            paraphrases = pipeline.paraphrase(input_text)
            if paraphrases and isinstance(paraphrases, list):
                st.markdown("#### ✅ Paraphrased Results")
                for i, p in enumerate(paraphrases, 1):
                    st.markdown(f"<div class='output-box'><b>Version {i}</b><br>{p}</div>", unsafe_allow_html=True)
                    st.download_button(f"⬇️ Download Paraphrase {i}", p, f"paraphrase_{i}.txt")
            else:
                st.warning("No paraphrases generated.")

    else:
        st.info("👈 Enter text and click a button to get started!")

# Footer
st.markdown("<div class='footer'>Built with ❤️ using Streamlit • Hugging Face • Groq Cloud</div>", unsafe_allow_html=True)
