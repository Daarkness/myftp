

class FileException(Exception):
    def __init__(self,pathname):
        super().__init__(pathname)
        self.pathname = pathname


class PathNotExists(FileException):
    pass 