from File import Ftp_File
import os


class Ftp_Common:

    def __init__(self):

        self.Ftp_func = [
            "login",
            "cd",
            "send",
            "get"
        ]

    def Create_Msg(self,func_str,data,token=None):
        msg = {
            "func":func_str,
            "data":data,
            "token":token}
        return msg

class Ftp_Exception(Exception):
    def __init__(self,err_msg):
        super().__init__("ERROR : {}..".format(err_msg))
        self.err_msg  = err_msg

