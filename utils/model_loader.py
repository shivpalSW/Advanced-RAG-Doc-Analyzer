
import os
import sys
from dotenv import load_dotenv
from utils.config_loader import load_config
from .config_loader import load_config
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

# Initialize logger. This should be done after imports to avoid circular dependencies
# Ensure the logger is initialized only once
log = CustomLogger().get_logger(__name__)


class ModelLoader: 
    
    """
    A utility class to load embedding models and LLM models.
    """
    
    def __init__(self):
       pass
        
    def _validate_env(self):
       pass
        
    def load_embeddings(self):
       pass
        
    def load_llm(self):
       pass
    
    
if __name__ == "__main__":
    loader = ModelLoader()
  