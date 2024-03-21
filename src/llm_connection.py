import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI



def llm_connection():
    load_dotenv()
    llm = GoogleGenerativeAI(model="gemini-pro",google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.2)
    return llm