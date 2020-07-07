from nbNet.nbNetFramework import nbNet
from Ftp_Com import Ftp_Common
from User import User,User_Auth
from server_conf import User_conf


import os
'''
def logic(d_in):
    print(d_in)
    return ("ok")
resD = nbNet('0.0.0.0',8000,logic)
'''

class ftp_server(nbNet,Ftp_Common):
    def __init__(self,ip,port,base_path):

        self.Server = nbNet.__init__(self,ip,port,self.logic)
        self.Ftp = Ftp_Common.__init__(self,base_path)
        self._Auth = User_Auth()
        self._Base_Path = os.path.join(os.getcwd(),"data")
        print(self._Base_Path)
        #init ftp setting
        self.init_conf()

    def init_conf(self):
        users_conf = User_conf
        for username,password in users_conf.items():
            self._Auth.add_user(username,password)






    def logic(self,d_in):
        return "123"


ret =ftp_server('0.0.0.0',8000,os.path.join(os.getcwd(),"data"))
ret.run()


