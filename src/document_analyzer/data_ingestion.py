import os 
import fitz # PyMuPDF
import uuid
from datetime import datetime
from logger .custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentHandler():
     """
     Handles PDF saving and reading operations.
     Automatically logs all actions and supports session-based organization.
     """
     def __init__(self,data_dir=None,session_id=None):
        try:
            self.log=CustomLogger().get_logger(__name__)
            self.data_dir = data_dir or os.getenv(
                "DATA_STORAGE_PATH",
                os.path.join(os.getcwd(), "data", "document_analysis")
            )
            self.session_id = session_id or f"session_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
            
            # Create base session directory
            self.session_path = os.path.join(self.data_dir, self.session_id)
            
            os.makedirs(self.session_path, exist_ok=True)

            self.log.info("PDFHandler initialized", session_id=self.session_id, session_path=self.session_path)

        except Exception as e:
            self.log.error(f"Error initializing DocumentHandler: {e}")
            raise DocumentPortalException("Error initializing DocumentHandler", e) from e
        

     def save_pdf(self,pdf_data):
        """
        Saves the PDF data to a file in the session directory.        
        Saves the PDF document to a specified location with a unique filename.
        pass
        """
        try:
            pass
        
        except Exception as e:
            self.log.error(f"Error saving PDF: {e}")
            raise DocumentPortalException("Error saving PDF", e) from e

     

     def read_pdf(self):
         """
         Reads the PDF document and extracts text from each page.
         :return: A list of strings, each representing the text of a page.
         """
         try:
             pass
         
         except Exception as e:
             self.log.error(f"Error saving PDF: {e}")
             raise DocumentPortalException("Error saving PDF", e) from e
         
if __name__ == "__main__":
    handler = DocumentHandler()