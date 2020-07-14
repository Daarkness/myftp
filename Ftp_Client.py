from Ftp_Com import Ftp_Common
from Client import Client_Net
from Memu import memu
from User import User

import json

class Ftp_Client(Client_Net,Ftp_Common):
    def __init__(self,server_ip,server_port):
         self.Net = Client_Net(server_ip,server_port)
         self.Ftp = Ftp_Common.__init__(self)
         self.Memu = memu()
         self.User_Obj = None
         self._Token  = None
         print(self.Net)


    def _ftp_login(self):
        username,password = self.Memu.login()
        self.Uesr_Obj = User(username,password)
        data = {
                "username":self.Uesr_Obj.username,
                "password":self.Uesr_Obj.password,
                }
        login_msg = self.Create_Msg("login",data)
        print(self.Net)
        res = self.Net.sendData(json.dumps(login_msg))

        print(res)



    def run(self):
        self._ftp_login()









client =  Ftp_Client("127.0.0.1",8000)
client.run()
