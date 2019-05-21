
class  InitExceptions(Exception):
    def __init__(self,stepname):
        super().__init__(stepname)
        self.stepname = stepname
 