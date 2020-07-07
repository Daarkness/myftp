from File import Ftp_File
import os


class Ftp_Common:

    def __init__(self,base_path):

        self.Base_Path = base_path
        '''
        self.msg = {
            "id":xxxxx,
            "msg":xxxxxx,
            "token":xxxxxx,
        '''
        self.files = {}


    '''
    def get_msg_type(self,file_path):
        if os.path.exists(file_path):
            return "path"
        elif os.file.exists(file_path):
            return "file"
        else:
            return False
    '''


class Ftp_Exception(Exception):
    def __init__(self,err_msg):
        super().__init__("ERROR : {}..".format(err_msg))
        self.err_msg  = err_msg
#raise Ftp_Exception("1")
