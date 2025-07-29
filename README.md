
# 💻 Multi-Language AI Coding Tutor Agent

## 📝 Project Overview

The Multi-Language AI Coding Tutor Agent helps beginners learn essential programming concepts across **Python**, **C**, **C++**, **Java**, and **JavaScript**. The agent provides simple explanations, beginner-friendly code examples, curated YouTube resources, commonly asked coding questions, and small project suggestions to reinforce learning.

This AI agent is powered by **Ollama's phi3:mini model** and built with **Streamlit**, providing an interactive, easy-to-use learning platform for aspiring developers.

---

## ⚙️ Technical Approach

- Uses **Ollama LLM** (`phi3:mini`) to generate beginner-friendly educational content.
- Built with **Streamlit** for a clean, interactive interface.
- Aligns all feature buttons in a single row for easy navigation.
- Removes unnecessary `<think>` blocks from AI output using regular expressions.
- Provides YouTube video suggestions with direct search links.
- Modular, maintainable code structure for easy extension.

---

## 🚀 Features

✅ Beginner-friendly concept explanations  
✅ Clear, well-commented code examples  
✅ Curated YouTube video suggestions with direct links  
✅ Most asked coding/interview questions for selected concepts  
✅ Small project suggestions to apply learning  

---

## 🖥 Setup & Running the Agent (Step-by-Step)

### 1. Clone the Repository

```bash
git clone https://github.com/Vemula-Bhavani/Coding-Tutor-Agent.git
cd Coding-Tutor-Agent
git checkout feature/ai-agent
```

### 2. Setup Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment:

- **On Windows:**

```bash
.venv\Scripts\activate
```

- **On Mac/Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run main.py
```

---

## 🧪 Testing the AI Agent

1. Select a programming language from the dropdown.
2. Enter a concept you'd like to learn (e.g., *Lists*, *Loops*, *Functions*).
3. Click the feature buttons to:
   - Get beginner-friendly explanations  
   - See relevant code examples  
   - Explore YouTube resources  
   - View commonly asked coding questions  
   - Get small project suggestions  
4. **Verify output is clean, relevant, and does not contain `<think>` blocks or extra reasoning.**

---

## 🛠 Technologies Used

- Python  
- Streamlit  
- Ollama LLM (`phi3:mini`)  
- Regular Expressions for output cleanup  

---

## 🎯 Key Learnings

- Integrated LLMs with prompt engineering for beginner-focused educational tools.  
- Used Streamlit to build an accessible AI-powered learning platform.  
- Applied regular expressions to refine AI output.  
- Explored AI agent development workflow suitable for hackathons.  

---

## 🎥 Demo Video

➡️ https://youtube.com/shorts/ffFT5HtG154?si=CmDGA0IxZEUSmdzF

---



## 📝 Additional Notes

This project demonstrates a lightweight AI educational agent ideal for beginners.  
Future improvements may include YouTube API integration, interactive quizzes, and additional language support.

---


