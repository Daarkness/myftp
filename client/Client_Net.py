from client import clientnet_exceptions


import socket 
class clinet_net:
    def __init__(self,host,port):
        self.host =  host
        self.port = port 
        sesock_l = []


    def connect_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host,self.port))
        return sock 
    def sendData(self,data):
        retry = 0 
        while retry < 3:
            try:
                if sock_l[0] == None:
                    sock_l[0] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock_l[0].connect((host, port))
                   
                d = data
                sock_l[0].sendall("%010d%s"%(len(d), d)) 
                
                count = sock_l[0].recv(10)
                if not count:
                    raise Exception("recv error", "recv error")
                count = int(count)
                buf = sock_l[0].recv(count)
                  
                if buf[:2] == "OK":
                    retry = 0 
                    break
            except:
                sock_l[0].close()
                sock_l[0] = None
                retry += 1
    