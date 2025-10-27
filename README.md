# 📝 TextMorph — Text Summarizer & Paraphraser  

An advanced **Streamlit-based NLP application** that performs **Extractive and Abstractive Text Summarization** and **Paraphrasing** using state-of-the-art Transformer models.  
Built with modular architecture, YAML configuration management, and a custom CSS-enhanced interface.  

---

## 🚀 Features
- ✨ **Abstractive Summarization** – Generates new phrasing using transformer models  
- 🧩 **Extractive Summarization** – Selects the most meaningful sentences directly from the text  
- 🔄 **Paraphrasing** – Creates multiple rewritten versions of your input  
- ⚙️ **Config-Driven Architecture** – Easily customize models, parameters, and keys in `config.yaml`  
- 🪵 **Logging & Error Handling** – Manageable and extendable structure for debugging  
- 🎨 **Styled UI** – Clean Streamlit interface with subtle CSS enhancements  
- 💾 **Download Output** – Save summaries or paraphrases as `.txt` files  

---

## 🛠️ Project Structure


textmorph/
│
├── mvp/
│   ├── __init__.py
│   ├── extractive.py
│   ├── abstractive.py
│   ├── paraphraser.py
│   └── mvp_pipeline.py
│
├── config.yaml
├── config_manager.py
├── app.py
├── requirements.txt
└── .env


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/lakshita07232308/textmorph.git](https://github.com/lakshita07232308/textmorph.git)
cd textmorph
```
### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate    # For Windows
# or
source .venv/bin/activate # For macOS/Linux
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Configure Environment Variables
Copy `.env.example` to `.env` and add your Hugging Face key:
```bash
HF_API_KEY=your_huggingface_api_key
```
### 5️⃣ Run the App
```bash
streamlit run app.py
```
--- 

## 💡 How to Use

1.  Open the local URL shown in your terminal.
2.  Paste or type the text you want to summarize or paraphrase.
3.  Choose the **Summarization Method** (Extractive / Abstractive).
4.  Select **Summary Length** (Short / Medium / Long).
5.  Click **Summarize** or **Paraphrase**.
6.  Download your result as `.txt` if needed.

---

## ⚡ Technologies Used

-   🧠 **Transformers** (Hugging Face)
-   🔥 **PyTorch**
-   🧮 **NLTK & NumPy**
-   💡 **Streamlit** (Frontend)
-   📜 **YAML** Configuration
-   🧰 **Python-dotenv**
-   🎨 **Custom CSS** Styling

---

## 👩‍💻 Author

-   **Lakshita Setia**
-   📧 `lakshita07232308@gmail.com`
-   🌐 [GitHub Profile](https://github.com/lakshita07232308)

---

