# 📚 Genre-Blended Story Generator

A modern, AI-powered storytelling app that lets you **create, continue, and manage episodic stories** — blending genres like **Mythology, Sci-Fi, Mystery, and Thriller**, all powered by a **lightweight local LLM (Phi-2 via Ollama)**.

> 🧠 Built with ❤️ using Streamlit and Ollama, this app runs 100% offline and generates immersive, character-driven episodes with cliffhangers.

---

## ✨ Features

- 🎭 **Genre + Prompt-Based Storytelling**
- 🔄 **Continue previous episodes** with narrative memory
- 📁 **Saves episodes** as plain text per story
- 🧠 **Runs locally with Phi-2 via Ollama** — no API keys or internet required
- 🧩 **Smart prompt chaining** ensures story continuity and drama

---

## 🛠 Tech Stack

| Tool        | Purpose                            |
|-------------|------------------------------------|
| 🐍 Python    | Backend scripting & logic          |
| 🌐 Streamlit | Interactive UI                     |
| 🧠 Ollama    | LLM runner (Phi-2 or compatible)   |
| 📝 Markdown  | Episode formatting and storage     |

---

## 🚀 Installation & Usage

### ✅ Prerequisites

- Python 3.10 or higher
- [Ollama installed](https://ollama.com/download) (for running the local AI model)

---

### 📦 Step 1: Install Python dependencies

```bash
pip install streamlit requests
ollama run phi
streamlit run app.py

