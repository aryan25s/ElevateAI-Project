import streamlit as st
import pandas as pd
import google.generativeai as genai
from langchain.agents import create_openai_functions_agent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os

from dotenv import load_dotenv
load_dotenv()  # Load before using the API key
try:
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        st.error("API key not found! Check your .env file")
        st.stop()
        
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Configuration error: {str(e)}")
    st.stop()

generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

st.set_page_config(
        page_title="About Elevate.AI",
        page_icon="👩‍💻"
    )
st.title("AI SEO Assistant with Gemini API")
st.subheader("Leverage AI to optimize your content for SEO")

user_input = st.text_input("Enter Content or Topic for SEO Suggestions")

prompts_parts=[
        f"Suggest SEO-friendly keywords for the following text or topic: {user_input} and Optimize the following content for SEO, including suggestions for better keyword density, title tags, and headings."
    ]
response = model.generate_content(prompts_parts)


sumbit_button = st.button("Generate Blog")

if sumbit_button:
    if not user_input.strip():
        st.warning("Please enter some text first!")
    else:
        try:
         st.subheader("SEO Recommendations")
         st.write(response.text)
        except Exception as e:
            st.error(f"API Error: {str(e)}")

st.caption("<p style ='text-align:center'>Made with ❤️ by Kartikeya</p>",unsafe_allow_html=True)