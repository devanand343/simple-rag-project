# 📘 Project Title: Simple RAG System

## 🧠 Description
A Retrieval-Augmented Generation (RAG) tool that queries a vector database and provides concise answers (max 100 words) via CLI or Streamlit.

---

## ✨ Features

- **CLI Interface**  
  Run queries directly from the terminal via `main.py`.

- **Web Interface**  
  Interactive UI built with Streamlit in `app.py`.

- **Modular Logic**  
  Core RAG operations separated into the `logic/` folder.

- **Security**  
  API keys managed via `.env` files.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd <your-repo-folder>
```

### 2. Create a Virtual Environment
```bash
python -m venv .myenv
source .myenv/bin/activate  # On Windows: .myenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
```bash
OPENAI_API_KEY=your_actual_key_here
```

## 🚀 Usage

### Run the CLI
```bash
python main.py
```

### Run the Streamlit App
```bash
streamlit run app.py
```

## 📁 Project Structure

- `main.py`  
  Entry point for the CLI application.

- `app.py`  
  Entry point for the Streamlit web application.

- `logic/`  
  Contains the backend logic for document processing and vector database queries.

- `.env.example`  
  A template for required environment variables.

  
