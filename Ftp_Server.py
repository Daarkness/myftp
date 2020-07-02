from nbNet.nbNetFramework import nbNet


def logic(d_in):
    print(d_in)
    return ("ok")


resD = nbNet('0.0.0.0',8000,logic)

class fpt_server(nbNet,Ftp):
    pass
