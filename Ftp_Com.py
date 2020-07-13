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



class Ftp_Exception(Exception):
    def __init__(self,err_msg):
        super().__init__("ERROR : {}..".format(err_msg))
        self.err_msg  = err_msg
