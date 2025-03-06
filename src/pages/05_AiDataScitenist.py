import streamlit as st
from langchain.document_loaders.csv_loader import CSVLoader
import tempfile
import pandas as pd
import  google.generativeai as genai
from utilis import get_model_response
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv
load_dotenv()  # Load before using the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Set your Google Gemini API Key
google_gemini_key = api_key
genai.configure(api_key=google_gemini_key)
with st.sidebar:
    st.write("*Unleash the power of your data with my AI assistance!*")
    st.caption("""I'm ready to dive deep into your numbers, uncover hidden patterns, and deliver actionable insights. But first, we need a solid foundation. 
             Please upload your CSV file 📂 so we can embark on this data-driven journey together. 
             Let's transform your raw information into valuable knowledge.Sounds fun right , let's go!!
             """)
    with st.expander("What are the steps for EDA"):
       st.write(
           #llm.invoke("What are the steps for EDA").content
           )
    st.divider()
    st.caption("<p style ='text-align:center'>Made with ❤️ by Kartikeya</p>",unsafe_allow_html=True)


def main():
    st.title("Ask your csv")
    st.subheader("")

    user_csv = st.file_uploader(
        "upload your csv file ",
        type="csv"
    )
    if user_csv is not None:
        user_question = st.text_input("Ask a question about your csv: ")
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.9,
            api_key=google_gemini_key
    
        )
        agent = create_csv_agent(
            llm,
            user_csv,
            verbose=True,
            allow_dangerous_code=True

        )
        if user_question is not None and user_question!="":
            response = agent.run(user_question)
            st.write(f"Your question was :{user_question}")
            st.write(f"response:{response}")
            
          
main()


