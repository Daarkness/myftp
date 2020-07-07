from client import clientnet_exceptions


import socket 
class clinet_net:
    def __init__(self,host,port):
        self.host =  host
        self.port = port 
        self.sock_l=[None]
      

    def connect_server(self):
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host,self.port))
        return sock 

    def sendData(self,data):
        retry = 0
        while retry < 3:
            try:
                print(self.sock_l[0])
                if self.sock_l[0] == None:
                    self.sock_l[0] = self.connect_server()
                print(type(data))
                self.sock_l[0].sendall(bytes("%010d%s"%(len(data), data),encoding='utf-8') )
                count = self.sock_l[0].recv(10)
                if not count:
                    pass 
                        #raise Exception("recv error", "recv error")
                count = int(count)
                buf = self.sock_l[0].recv(count)
                return buf
            except ConnectionRefusedError as e:
                self.sock_l[0].close()
                self.sock_l[0] = None
                retry += 1

