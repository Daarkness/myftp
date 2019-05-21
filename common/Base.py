class base:
    _cmd_code_dict =  {
                "00001":"login",
                "00002":"logout",
                "00003":"ls",
                "00004":"cd",
                "00005":"get_file",
                "00006":"send_file",
    
        }
    _res_code_dict = {
                "10001":"msg is success",
                "20001":"server error",
                "20002":"Authentication failed",
                "20004":"Parameter failed"
    }
    
 
    def __init__(self,Authenticator=None,file_contor=None):
        self.Auth = Authenticator
        self.File_Contor = file_contor 
        #self.Work = work
        