import sys,os 
 
sys.path.insert(1, os.path.join(sys.path[0], '..'))


from common.Base import base 
from common import User,File_contor

from client import Views,Client_Net
from client.conf import server
import json 


class Agent(base):
    def __init__(self):
        super().__init__(file_contor=File_contor.file_contor)
        self._Net_model =  Client_Net.clinet_net(server['host'],server['port'])


    def login(self,User):
        send_msg = {
            "code": "00001",
            "data": {
                "username":User.username,
                "password":User.password
            }
        }
        self._Net_model.sendData(json.dumps(send_msg))
        print(send_msg)
        


    def process(self):
        view = Views.View()
        view.display()
        username,password = view.get_user_msg()        
        user_obj = User.User(username,password)
        self.login(user_obj)
     

    def run(self):
        self.process()

if __name__ == '__main__':
    agent = Agent()
    agent.run()
    