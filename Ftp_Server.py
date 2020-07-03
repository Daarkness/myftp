from nbNet.nbNetFramework import nbNet
from Ftp_Com import Ftp_Common

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


    def logic(self,d_in):
        return "123"

    def ftp_init()
ret =ftp_server('0.0.0.0',8000,os.path.join(os.getcwd(),"data"))
ret.run()


