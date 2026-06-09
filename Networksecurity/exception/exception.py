import sys
from Networksecurity.logging.logger import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename
    def __str__(self):
        return f"Error occured in script [{self.filename}] at line number [{self.lineno}] with error message [{self.error_message}]"
        self.filename,self.lineno,str(self.error_message)
    
if __name__=="__main__":
    try:
        logger.info("Testing the NetworkSecurityException class.")
        a=1/0
    except Exception as e:
        logger.info("Divide by zero error occurred.")
        raise NetworkSecurityException(e,sys)
