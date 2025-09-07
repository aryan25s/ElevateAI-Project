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
def main():
    st.set_page_config(page_title="AI Data Scientist", page_icon="🤖")
    st.title("AI Data Scientist Assistant")
    
    with st.sidebar:
        st.write("*Unleash the power of your data!*")
        st.caption("""Upload your CSV file to analyze patterns and generate insights.""")
        st.divider()
        st.caption("<p style='text-align:center'>Made with ❤️ by Aryan</p>", unsafe_allow_html=True)

    # File uploader
    user_csv = st.file_uploader("Upload CSV", type="csv")
    
    if user_csv:
        # Read CSV to DataFrame
        df = pd.read_csv(user_csv)
        st.write("Data Preview:")
        st.dataframe(df.head())
        
        # Initialize LLM
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.6,  
            google_api_key=api_key
        )
        
        # Create agent
        agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=True,
            allow_dangerous_code=True
        )
        
        # Question input
        user_question = st.text_input("Ask about your data:")
        if user_question:
            try:
                response = agent.run(user_question)
                st.subheader("Analysis Result")
                st.write(response)
            except Exception as e:
                st.error(f"Error analyzing data: {str(e)}")

if __name__ == "__main__":
    main()