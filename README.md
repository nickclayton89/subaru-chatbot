# 🚗 Subaru Sales Assistant Chatbot

An AI-powered chatbot built with Streamlit and LangChain to answer questions about 2025 Subaru models (Crosstrek, Forester, etc.) using local documents and OpenAI embeddings.

---

## 💡 Features

- Ask natural language questions about Subaru vehicle specs, trims, features, etc.
- Powered by Retrieval-Augmented Generation (RAG) using LangChain
- Embeds local data files with FAISS for fast retrieval
- Easily extendable with new vehicle data
- Runs on Streamlit Cloud or locally

---

## 🧠 Technologies Used

- Python 3.10+
- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)
- [FAISS](https://github.com/facebookresearch/faiss)

---

## 📁 Project Structure

subaru-chatbot/
├── app.py # Main Streamlit app
├── data/
│ ├── 2025_crosstrek.txt # Text content for Crosstrek
│ └── 2025_forester.txt # Text content for Forester
├── requirements.txt # Python dependencies
└── README.md # You're here

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/subaru-chatbot.git
cd subaru-chatbot
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set your OpenAI API key
Create a .env file or set the key in your terminal:

bash
Copy
Edit
export OPENAI_API_KEY=your-openai-api-key
Or in .streamlit/secrets.toml if using Streamlit Cloud:

toml
Copy
Edit
OPENAI_API_KEY = "your-openai-api-key"
4. Run the app
bash
Copy
Edit
streamlit run app.py
➕ Adding More Vehicle Data
Create a new .txt file in the data/ folder (e.g. 2025_outback.txt)

Use structured markdown or bullet format

Update the file list in app.py:

python
Copy
Edit
for file in [
    "data/2025_crosstrek.txt",
    "data/2025_forester.txt",
    "data/2025_outback.txt"
]:
🧪 Example Questions
"What is the ground clearance of the 2025 Crosstrek Wilderness?"

"Which trim levels offer the Harman Kardon sound system?"

"How much can the Forester tow?"

🛠 Troubleshooting
If you see RateLimitError or AuthenticationError:

Make sure your OpenAI API key is correct and active

Switch to gpt-3.5-turbo to reduce cost and hit fewer rate limits

Upgrade to a paid OpenAI plan if using free-tier

📄 License
MIT License — free to use and modify.

