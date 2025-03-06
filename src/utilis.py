from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv
load_dotenv()  # Load before using the API key
api_key = os.getenv("GOOGLE_API_KEY")

# Set your Google Gemini API Key
google_gemini_key = api_key
genai.configure(api_key=google_gemini_key)
os.environ["Google_API_KEY"]=google_gemini_key

def get_model_response(file,query):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=200)
    context = "\n\n".join(str(p.page_content)for p in file)
    data = text_splitter.split_text(context)
    if not data:
        print("Error: No data to process.")
        return
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    Searcher = Chroma.from_texts(data,embeddings).as_retriever()

    q= "which employee has maximum salary?"
    records = Searcher.get_relevant_documents(q)
    print(records)

