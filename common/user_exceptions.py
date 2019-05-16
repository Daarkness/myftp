class AuthException(Exception):
    def __init__(self,username,user):
        super().__init__(username,user)
        self.username = username 
        self.user = user 


class UsernameAlreadyExists(AuthException):
    pass

class PassWordtooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass