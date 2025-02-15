import streamlit as st
import  google.generativeai as genai
import os

from dotenv import load_dotenv
load_dotenv()  # Load before using the API key
api_key = os.getenv("Google_Gemini_key")

# Set your Google Gemini API Key
google_gemini_key = api_key
genai.configure(api_key=google_gemini_key)

# Create the model
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

st.title("AI Customer Feedback & Sentiment Analysis Tool")
st.subheader("Analyze and gain insights from customer feedback")

user_input = st.text_area("Enter the customer feedback and get insights",height=200)

prompts_parts=[
        f"Given the following user input, provide detailed and constructive feedback. Address any positive aspects and suggest areas of improvement where necessary. Ensure your tone is supportive, professional, and focused on helping the user improve or better understand their feedback.Analyze the sentiment of the following feedback: {user_input} .\n User Input: {user_input} \n Feedback. "
    ]
response = model.generate_content(prompts_parts)


sumbit_button = st.button("Generate Sentiment analysis")

if sumbit_button:
    st.write(response.text)

st.caption("<p style ='text-align:center'>Made with ❤️ by Kartikeya</p>",unsafe_allow_html=True)