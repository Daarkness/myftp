import os

class Ftp_File:
    def __init__(self,file_path):
        self.file_path = file_path
        self.file_size = file_size
        self.file_fd =  file_fd

    def Close_File(self):
        self.file_fd.close()

    def get_file_fd(file_path):
        try:
            file_fd = open(file_path,"r+")
            file_size =  os.path.getsize(file_path)
        except ValueError as e:
            print(e)
        else:
            return  (file_fd,file_size)
        return None

    staticmethod(get_file_fd)

