
import os 

from common import file_contor_exceptions

class file_contor:
    def __init__(self,work_path):
        self._work_path = work_path
        self.files  = {}
    def _set_work_path(self,work_path):
        self._work_path = work_path
        pass
    def _get_work_path(self):
        return self._work_path

    def check_path(self):
        if not os.path.isdir(self.work_path):
            raise file_contor_exceptions.PathNotExists(self.work_path)
    
    work_path = property(_get_work_path,_set_work_path)

    
