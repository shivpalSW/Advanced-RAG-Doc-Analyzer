import sys
from dotenv import load_dotenv
import pandas as pd
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from prompt.prompt_library import PROPMT_REGISTRY
from utils.model_loader import ModelLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

class DocumentComparatorLLM:
    """
    # A class to handle document comparison using LangChain.
    # This class uses LangChain to compare documents and extract differences.
    # It also uses PyMuPDF to extract metadata from PDF documents.
    # This class is designed to compare two documents and return a structured comparison.
    """
    def __init__(self):
        
        load_dotenv()
        self.log = CustomLogger().get_logger(__name__)
        self.loader = ModelLoader()
        self.llm = self.loader.load_llm()
        self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm=self.llm)
        self.prompt = PROPMT_REGISTRY["document_comparison"]
        self.chain = self.prompt | self.llm | self.parser | self.fixing_parser
        self.log.info("DocumentComparatorLLM initialized with model and parser.")
    
    def compare_documents(self):
        """
        Compares two documents and returns a structured comparison.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in compare_documents: {e}")
            raise DocumentPortalException("An error occurred while comparing documents.",sys)
    
    def _format_response(self):  # private method
        """
        Formats the response from the LLM into a structured format.
        """
        try:
            pass
        except Exception as e:
            self.log.error("Error formatting response into DataFrame", error=str(e))
            raise DocumentPortalException("Error formatting response",sys)