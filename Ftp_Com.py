from File import Ftp_File

class Ftp_Common:
    def __init__(self):
        self.files = {}

    def add_file(self,file_path):

        Ftp_File.get_file_fd(file_path)

        pass


