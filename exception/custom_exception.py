import sys
import traceback
from logger.custom_logger import CustomLogger

logger =CustomLogger().get_logger(__file__) # Initialize the logger here 
# __FILE__ is a special variable that contains the name of the current Python file`

class DocumentPortalException(Exception):
    """Custom exception for Document Portal"""
    def __init__(self,error_message,error_details:sys):
        print(error_details.exc_info())# Debugging purpose
        _,_,exc_tb=error_details.exc_info() # Get the traceback object
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno # Get the line number where the exception occurred
        self.error_message=str(error_message)# Convert the error message to string
        # Format the traceback for better readability
        self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info())) # Convert the traceback to a string

    def __str__(self):# Override the string representation of the exception
        """Return a formatted string representation of the exception"""
        return f"""
        Error in [{self.file_name}] at line [{self.lineno}] 
        Message: {self.error_message}
        Traceback:
        {self.traceback_str}
        """
    
if __name__ == "__main__":# Main function to run the script
    # Main function to demonstrate the custom exception
    try:
        # Simulate an error
        a = 1 / 0
        print(a) 
    except Exception as e:
        app_exc=DocumentPortalException(e,sys)# sys,Create an instance of the custom exception
        logger.error(app_exc)
        raise app_exc