import sys

def error_msg_details(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "python scripy file name: {0} - line number {1} - error_message {2}".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_msg_details(error_message, error_detail)

    def __str__(self):
        return self.error_message