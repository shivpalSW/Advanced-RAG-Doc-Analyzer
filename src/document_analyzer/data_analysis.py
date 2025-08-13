import os
import sys
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from prompt.prompt_library import *


class DocumentAnalyzer:
    """
    # A class to handle document analysis and metadata extraction.
    # This class uses LangChain to analyze documents and extract metadata.
    """

    def __init__(self):
        """
        Initialize the DocumentAnalyzer class.
        This method sets up the necessary components for document analysis.
        """
        self.log = CustomLogger().get_logger(__name__)
        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_llm()

            # Prepare parsers
            self.parser = JsonOutputParser(pydantic_object=Metadata)
            self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm=self.llm)

            self.prompt = prompt

            self.log.info("DocumentAnalyzer initialized successfully")

        except Exception as e:
            self.log.error(f"Error initializing DocumentAnalyzer: {e}")
            raise DocumentPortalException("Error in DocumentAnalyzer initialization", sys)

    def analyze_document(self):
        """
        Analyzes the metadata of the document.
        :param document_path: Path to the document to be analyzed.
        :return: Metadata of the document.
        """
        pass