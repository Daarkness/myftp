class base:
    cmd_list =  {
                "00001":"pwd",
                "00002":"ls",
        }
 
    def __init__(self,Authenticator,file_contor):
        self.Auth = Authenticator
        self.File_Contor = file_contor 
        