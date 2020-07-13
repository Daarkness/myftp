from nbNet.nbNetFramework import nbNet
from Ftp_Com import Ftp_Common
from User import User,User_Auth
from server_conf import User_conf,Base_Dir,Disk_Quota


import os
class ftp_server(nbNet,Ftp_Common):
    def __init__(self,ip,port,base_path):

        self.Server = nbNet.__init__(self,ip,port,self.logic)
        self.Ftp = Ftp_Common.__init__(self,base_path)
        self._Auth = User_Auth()
        self._Base_Path = os.path.join(os.getcwd(),"data")
        self.Token_Map={}
        #init ftp setting
        self.init_conf()

    def init_conf(self):

        print("---init confing---")
        users_conf = User_conf
        for username,password in users_conf.items():
            self._Auth.add_user(username,password,Disk_Quota[username],os.path.join(self._Base_Path,username))

        self._Base_Path = Base_Dir
        for k,v in self._Auth.users.items():
            print(k,v.disk_quata,v.home_path)

        print("---init sussuss---")

    def logic(self,d_in):
        return "123"


server =ftp_server('0.0.0.0',8000,os.path.join(os.getcwd(),"data"))
server.run()


