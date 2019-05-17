import sys,os 
 
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from nbNet import nbNetFramework 
from common.Base import base 
from common import User,user_exceptions

from server import server_exceptions as ser_ex 

from  conf import server,changeroot,users
class Server(base):
    def __init__ (self,ip,port,Change_root_path):
        self.ip = ip
        self.port = port 
        self._Net_model =  nbNetFramework.nbNet


    def download(self,filename):
        pass

    def update(self,filename):
        pass 

    def _User_load(self,users_dict):
        Authenticator = Authenticator() 
        for username,password in users_dict.items():
            Authenticator = User.Authenticator()
            try:
                Authenticator.add_user(username,password)
            except user_exceptions.UsernameAlreadyExists:
                return False InitExceptions
        return Authenticator 


    def logic(self,d_in):
        
        return(d_in)
    def run(self):
        Authenticator = self._User_load(users)
        if not Authenticator:
            raise  
        '''
        初始化
        主流程
        '''

        self._Net_model(self.ip,self.port,self.logic('d_in'))

if __name__ == '__main__':


    server =  Server(server['ip'],server['port'],changeroot)
    server.run()
  