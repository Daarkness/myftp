import sys,os 
 
sys.path.insert(1, os.path.join(sys.path[0], '..'))


from common.Base import base 
from common import User,File_contor

from client import Views,Client_Net




class Agent(base):
    def __init__(self):
        super().__init__(file_contor=File_contor.file_contor)
        self._Net_model =  Client_Net.clinet_net
    def run(self):
        '''
            打印欢迎消息
            获取用户名密码
            登录服务器
            等待用户输入
            将输入发动到服务器
        '''
        view = Views.View()
        view.display()
        username,password = view.get_user_msg()        
        user_obj = User.User(username,password)
        

        while 1:
            row_cmd = view.get_cmd()
            #获取命令后发送到服务端
    

if __name__ == '__main__':
    agent = Agent()
    agent.run()
    