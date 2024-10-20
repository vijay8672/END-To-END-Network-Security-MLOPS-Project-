import sys
from Network_security.logging import logger


class NetworkSecurityException(Exception):
  def __init__(self, error_message, error_detail:sys):
    self.error_message=error_message
    _,_,exc_tb=error_detail.exc_info()

    self.line_no=exc_tb.tb_lineno
    self.file_name=exc_tb.tb_frame.f_code.co_filename

  
  def __str__(self):
    return "Error occurred in python script name [{0}] line number [{1}] error message detail [{2}]".format(self.file_name,self.line_no, str(self.error_message))


if __name__=='__main__':
  try:
    logger.logging.info("Enter the try block")
    a=1/0
    print("Zero Division Error",a)

  except Exception as e:
    raise NetworkSecurityException(e,sys)
