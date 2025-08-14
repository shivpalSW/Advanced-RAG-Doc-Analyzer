import os
import sys
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from prompt.prompt_library import PROPMT_REGISTRY


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

            self.prompt = PROPMT_REGISTRY["document_analysis"]

            self.log.info("DocumentAnalyzer initialized successfully")

        except Exception as e:
            self.log.error(f"Error initializing DocumentAnalyzer: {e}")
            raise DocumentPortalException("Error in DocumentAnalyzer initialization", sys)

    def analyze_document(self,document_text:str)-> dict:
        """
        Analyze a document's text and extract structured metadata & summary.
        :param document_path: Path to the document to be analyzed.
        :return: Metadata of the document.
        :raises DocumentPortalException: If there is an error during analysis.
        """
        
        try:
            chain = self.prompt | self.llm | self.fixing_parser
            
            self.log.info("Meta-data analysis chain initialized")

            response = chain.invoke({
                "format_instructions": self.parser.get_format_instructions(),
                "document_text": document_text
            })

            self.log.info("Metadata extraction successful", keys=list(response.keys()))
            
            return response

        except Exception as e:
            self.log.error("Metadata analysis failed", error=str(e))
            raise DocumentPortalException("Metadata extraction failed",sys)