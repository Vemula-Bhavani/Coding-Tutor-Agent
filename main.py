import streamlit as st
import ollama
import re

st.set_page_config(page_title="Multi-Language Coding Tutor Agent", layout="wide")
st.title("💻 Multi-Language Coding Tutor Agent")

# Language selection
language = st.selectbox("Choose a programming language:", ["Python", "C", "C++", "Java", "JavaScript"])

# Concept input
topic = st.text_input(f"Enter a {language} concept you'd like to learn about:")

# Aligned action buttons
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    explain_btn = st.button("Explain Concept")
with col2:
    example_btn = st.button("Show Code Example")
with col3:
    youtube_btn = st.button("Recommend YouTube Videos")
with col4:
    faq_btn = st.button("Most Asked Coding Questions")
with col5:
    project_btn = st.button("Suggest Small Projects")

# Session state to store response
if "response" not in st.session_state:
    st.session_state.response = ""

# Function to interact with Ollama
def ask_ollama(prompt):
    try:
        response = ollama.chat(model="phi3:mini", messages=[
            {"role": "user", "content": prompt}
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

# Function to remove <think>...</think> block
def remove_think_block(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE).strip()

# Explain Concept
if explain_btn and topic:
    with st.spinner("Generating explanation..."):
        prompt = f"Explain the {language} concept '{topic}' in simple language for a beginner."
        response_text = ask_ollama(prompt)
        response_text = remove_think_block(response_text)
        st.session_state.response = response_text
    st.success("Explanation Ready!")
    st.markdown(st.session_state.response)

# Show Code Example
if example_btn and topic:
    with st.spinner("Generating code example..."):
        prompt = f"Provide a clear, beginner-friendly {language} code example for the concept '{topic}'. Include comments."
        response_text = ask_ollama(prompt)
        response_text = remove_think_block(response_text)
        st.session_state.response = response_text
    st.success("Code Example Ready!")
    st.code(st.session_state.response, language=language.lower() if language != "C++" else "cpp")

# Recommend YouTube Videos
if youtube_btn and topic:
    with st.spinner("Finding relevant YouTube videos..."):
        prompt = (
            f"Suggest 3 YouTube video titles for learning the {language} concept '{topic}'. "
            "Only provide the video titles, no reasoning, no explanations, no internal thoughts."
        )
        response_text = ask_ollama(prompt)
        response_text = remove_think_block(response_text)
    
    st.success("Video Recommendations Ready!")
    
    video_titles = response_text.strip().split("\n")
    
    for idx, title in enumerate(video_titles):
        if title.strip():
            search_query = title.replace(" ", "+")
            youtube_link = f"https://www.youtube.com/results?search_query={search_query}"
            st.markdown(f"**{idx + 1}. {title}**  \n[🔗 Watch on YouTube]({youtube_link})")

# Most Asked Coding Questions
if faq_btn and topic:
    with st.spinner("Generating most asked coding questions..."):
        prompt = (
            f"List 5 of the most commonly asked coding or interview questions related to the {language} concept '{topic}'. "
            "Keep the questions beginner-friendly and clearly formatted as numbered questions."
        )
        response_text = ask_ollama(prompt)
        response_text = remove_think_block(response_text)
        st.session_state.response = response_text
    st.success("Most Asked Questions Ready!")
    st.markdown(st.session_state.response)

# Suggest Small Projects
if project_btn and topic:
    with st.spinner("Generating project ideas..."):
        prompt = (
            f"List 3 beginner-friendly project ideas to practice the {language} concept '{topic}'. "
            "Only provide the project titles with short descriptions, no internal reasoning, no extra text."
        )
        response_text = ask_ollama(prompt)
        response_text = remove_think_block(response_text)
    
    st.success("Project Ideas Ready!")
    st.markdown(response_text)
