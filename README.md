# 📄 Chat with PDF using Streamlit + HuggingFace

A lightweight app that lets you **upload PDF files and ask questions about their content** using **Flan-T5** and **FAISS-based semantic search**.

Built with:
- 🔍 HuggingFace Transformers
- 🧠 Langchain + FAISS for retrieval
- 🖥️ Streamlit for UI

---

## 🚀 Features

✅ Upload one or more PDF files  
✅ Extracts text from first 10 pages of each PDF  
✅ Splits content into smart chunks  
✅ Embeds using `all-MiniLM-L6-v2`  
✅ Answers your questions using `flan-t5-base`  
✅ Fast and accurate short answers (5–6 lines)

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/chat-with-pdf.git
cd chat-with-pdf

```
Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

```
Install dependencies
```bash
pip install -r requirements.txt

```
Create a .env file
```bash
touch .env
Add your Hugging Face token to it:
```
Add your Hugging Face token to it:
```env
Copy
Edit
HUGGINGFACE_API_KEY=your_huggingface_token_here
```
💡 You can get your token from: https://huggingface.co/settings/tokens

▶️ Run the App
```bash
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

🧠 Models Used
LLM: google/flan-t5-base

Embeddings: sentence-transformers/all-MiniLM-L6-v2

📂 Folder Structure
```csharp
chat-with-pdf/
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
🔐 Security
API keys are stored in .env (never committed to Git).

.env is in .gitignore to prevent accidental upload.

🧪 Example Use Cases
Upload your syllabus and ask questions

Upload a research paper and get summaries

Chat with PDF documentation or tutorials

## Working
![PdfChat-gif](https://github.com/user-attachments/assets/38dbc469-5732-4684-8e13-20edaa0bd585)


🛠️ Future Improvements
Add full chat history

Summarize entire documents

Add support for image-based PDFs (OCR)

Deploy to Hugging Face or Streamlit Cloud

