import sys,os 
 
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from nbNet import nbNetFramework 
from common.Base import base 
from common import User,user_exceptions,File_contor
from server import server_exceptions as ser_ex 
from common import file_contor_exceptions as file_con_exc 
from  conf import server,users,work_path




class Server(base):
    def __init__ (self,ip,port,work_path):
        self.ip = ip
        self.port = port 
        self._Net_model =  nbNetFramework.nbNet
        super().__init__(User.Authenticator(),File_contor.file_contor(work_path))

    def _User_load(self,users_dict):
        for username,password in users_dict.items():
            try:
                self.Auth.add_user(username,password)
            except Exception :
                return False 
        return True

    def _File_Path_load(self):
        try:
            self.File_Contor.check_path()
        except file_con_exc.FileException as msg:
            return False 
        else:
            return True 

    def logic(self,d_in): 
        #对客户端任务进行处理
        '''
            根据命令执行对应任务
        '''
    

        return(d_in)
        
    def start(self):
        #初始化
        '''
            导入用户
            设定工作目录
            等待登录
        '''
        print("------------start ftp --------------")
        Authenticator = self._User_load(users)
        if  not Authenticator:
            raise  ser_ex.InitExceptions("User load Error")
        else:
            print("[1] === User load Success")
        
        if not self._File_Path_load():
            raise ser_ex.InitExceptions("Path load Error")
        else:
            print("[2] === Path load Success")
        
        Net = self._Net_model(self.ip,self.port,self.logic)
        Net.run()

       
if __name__ == '__main__':

    server =  Server(server['ip'],server['port'],work_path)
    server.start()
  