import sys,os 
 
sys.path.insert(1, os.path.join(sys.path[0], '..'))


from common.Base import base 
from common import User,File_contor

from client import Views

class Agent(base):
    def __init__(self):
        pass

    def run(self):
        '''
            打印欢迎消息
            获取用户名密码
            等待用户输入
        '''
        view = Views.View()
        view.display()
        username,password = view.get_user_msg()        
        user = User.User(username,password)

        while 1:
            row_cmd = view.get_cmd()
            #获取命令后发送到服务端
    

if __name__ == '__main__':
    agent = Agent()
    agent.run()
    