import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

def get_github_api_key():
    return os.getenv("GITHUB_API_KEY")

# Streamlit app
st.title("Display GitHub API Key")

if st.button("Show API Key"):
    api_key = get_github_api_key()
    if api_key:
        st.write(f"GitHub API Key: {api_key}")
    else:
        st.write("API key not found. Please check your .env file and repository secrets.")
