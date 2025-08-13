import os 
import fitz # PyMuPDF
import uuid
from datetime import datetime
from logger .custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentHandler():

     """
     A class to handle document ingestion and processing using PyMuPDF.
     """

     def _init__(self, document_path: str):
         """
         Initializes the DocumentHandler with a document path.
         :param document_path: Path to the document to be processed.
         """
         pass

     def save_pdf(self):
          """
          Saves the PDF document to a specified location with a unique filename."""
          pass

     def read_pdf(self):
         """
         Reads the PDF document and extracts text from each page.
         :return: A list of strings, each representing the text of a page.
         """
         pass