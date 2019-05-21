class  Client_NetException(Exception):
    def __init__(self,Errorcode):
        super().__init__(self,Errorcode)
        self.Errorcode = Errorcode
