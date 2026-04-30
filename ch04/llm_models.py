from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv() #A
AZURE_OPENAI_BASE_URL = os.getenv("AZURE_OPENAI_BASE_URL")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL", "gpt-5.4-mini")

def get_llm(): #C
    return ChatOpenAI(model=AZURE_OPENAI_MODEL,
                 base_url=AZURE_OPENAI_BASE_URL,
                 api_key=AZURE_OPENAI_API_KEY)
#A Load the environment variables from the .env file
#B Get Azure OpenAI settings from the environment variables
#C Instantiate and return the ChatOpenAI model
