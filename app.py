import streamlit as st
import os
import requests
from datetime import datetime

# ---- CONFIG ----
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi"
BASE_DIR = "stories"

# ---- HELPER FUNCTIONS ----
def generate_episode(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    return response.json()['response']

def save_episode(story_name, episode_number, content):
    folder_path = os.path.join(BASE_DIR, story_name)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"Episode_{episode_number}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def load_story_episodes(story_name):
    folder_path = os.path.join(BASE_DIR, story_name)
    if not os.path.exists(folder_path):
        return []
    episodes = sorted([f for f in os.listdir(folder_path) if f.startswith("Episode")])
    return episodes

def read_episode(story_name, episode_filename):
    file_path = os.path.join(BASE_DIR, story_name, episode_filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# ---- STREAMLIT UI ----
st.set_page_config(page_title="Story Generator", layout="centered")
st.title("📚 Genre-Blended Story Generator")

menu = ["📝 New Story", "📖 Continue Story"]
choice = st.sidebar.radio("Select Mode", menu)

if choice == "📝 New Story":
    st.header("Start a New Story")
    story_name = st.text_input("Story Title")
    genres = st.text_input("Genres (e.g., Mythology + Sci-fi)")
    idea = st.text_area("Story Idea / Prompt")
    if st.button("Generate Episode 1") and story_name and idea:
        prompt = f"Title: {story_name}\nGenres: {genres}\nIdea: {idea}\n\nWrite Episode 1 of this story with a cliffhanger ending."
        episode = generate_episode(prompt)
        save_episode(story_name, 1, episode)
        st.success("Episode 1 generated and saved!")
        st.subheader("Episode 1:")
        st.text_area("", episode, height=400)

elif choice == "📖 Continue Story":
    st.header("Continue Existing Story")
    if not os.path.exists(BASE_DIR):
        st.warning("No stories found.")
    else:
        stories = sorted(os.listdir(BASE_DIR))
        selected_story = st.selectbox("Select Story", stories)
        episodes = load_story_episodes(selected_story)
        selected_episode = st.selectbox("Read Previous Episode", episodes[::-1])

        if selected_episode:
            prev_content = read_episode(selected_story, selected_episode)
            st.subheader(selected_episode)
            st.text_area("", prev_content, height=300)

            if st.button("Generate Next Episode"):
                next_ep_number = int(selected_episode.split("_")[1].split(".")[0]) + 1
                prompt = f"Continue this story as Episode {next_ep_number}, building on this previous episode:\n\n{prev_content}\n\nEnd with a cliffhanger."
                next_episode = generate_episode(prompt)
                save_episode(selected_story, next_ep_number, next_episode)
                st.success(f"Episode {next_ep_number} generated!")
                st.subheader(f"Episode {next_ep_number}:")
                st.text_area("", next_episode, height=400)
