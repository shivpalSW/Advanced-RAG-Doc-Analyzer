import os
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser


class DocumentAnalyzer():

     """
     # A class to handle document analysis and metadata extraction.
     # This class uses LangChain to analyze documents and extract metadata.
     """

     def __init__(self):
          pass

     def analyze_document(self):
         """
         Analyzes the metadata of the document.
         :param document_path: Path to the document to be analyzed.
         :return: Metadata of the document.
         """
         pass