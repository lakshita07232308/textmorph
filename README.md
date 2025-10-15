# TextMorph – AI Text Summarizer & Paraphraser

**TextMorph** is a web application that allows users to summarize and paraphrase text using AI-powered models via Hugging Face and Groq APIs. It supports both **extractive** and **abstractive summarization**, and generates **multiple paraphrased versions** of any input text — all without downloading heavy models locally.  

---

## Features
- **Extractive Summarization:** Selects key sentences from the original text.  
- **Abstractive Summarization:** Generates concise summaries in natural language.  
- **Paraphrasing:** Produces multiple reworded versions of the input text.  
- **Web-based UI:** Built with Streamlit for a user-friendly experience.  
- **API-based:** Uses Hugging Face / Groq APIs; no local models needed.  
- **Downloadable Outputs:** Save summaries or paraphrased text as `.txt`.  

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/textmorph.git
   cd textmorph
   
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   # macOS/Linux
   source .venv/bin/activate
   
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
4. **Set up API keys:**
   Copy `.env.example` to `.env`
   Add your Hugging Face API key (`HF_API_KEY`) and/or Groq API key (`GROQ_API_KEY`) in `.env`
   Example `.env`:
   ```bash
   HF_API_KEY=hf_your_huggingface_key_here
   GROQ_API_KEY=your_groq_key_here
    
5. **Run test script:**
   Tests summarization and paraphrasing functionality in the console.
   ```bash
   python test_run.py
   
6. **Run the Streamlit web app:**
   ```bash
   streamlit run app.py
   
- Open the URL in your browser.
- Paste your text.
- Choose Extractive or Abstractive summarization.
- Click Summarize or Paraphrase.
- Download results as `.txt` if needed.

---

## Technologies Used

- **Python 3.9+**
- **Streamlit** for the web UI
- **Hugging Face API** for summarization models
- **Groq API** for paraphrasing
- **Requests** for HTTP API calls
- **dotenv** for environment variable management
   
   
