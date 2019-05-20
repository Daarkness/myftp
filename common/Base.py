class base:
    cmd_list =  {
                "00001":"login",
                "00002":"logout",
                "00003":"ls",
                "00004":"cd",
                "00005":"get_file",
                "00006":"send_file",
        }
 
    def __init__(self,Authenticator,file_contor):
        self.Auth = Authenticator
        self.File_Contor = file_contor 
        