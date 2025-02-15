import streamlit as st
import  google.generativeai as genai
import os

from dotenv import load_dotenv
load_dotenv()  # Load before using the API key
api_key = os.getenv("Google_Gemini_key")

# Set your Google Gemini API Key
google_gemini_key = api_key
genai.configure(api_key=google_gemini_key)
st.title("Blogcraft : Your AI Writing Companion")

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

st.subheader("Now you can Craft Perfect Blogs with the help of AI")

with st.sidebar:
    st.title("Input Your Blog Details:")
    st.subheader("Enter Details of the Blog You want to generate")

    Blog_Title = st.text_input("Blog_Title")

    keyword =st.text_area("keywords(Comma-Separated)")

    num_words = st.slider("Number of Words",max_value=1000,min_value=250,step=250)
    prompts_parts=[
        f"generate a comprehensive, engaging blog post relevant to the title \" {Blog_Title} \"and the keywords \"{keyword}\".Make sure to incoporate these keywords in the blog post.The Blog should be approximately {num_words}  word in length, suitable for an online audience . Ensure the content is original , informative  and maintains a tone throughout."
    ]
    response = model.generate_content(prompts_parts)


    sumbit_button = st.button("Generate Blog")

if sumbit_button:
    st.write(response.text)