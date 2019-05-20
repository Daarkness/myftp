import hashlib
from common import user_exceptions
 
class Authenticator:
    def __init__(self):
        #用户认证       
        self.users = {}
    
    def add_user(self,username,password):

        if username in self.users:
            raise UsernameAlreadyExists
        self.users[username]= User(username,password)
    
    def login(self,username,password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        if not user.checkpassword(password):
            raise InvalidPassword(username,password)
        user.is_logged_in = True
        return True
    
    def logout(salf,username,password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        user.is_logged_in = False 
        return True

class User:
    #用户类
    def __init__(self,username,password):
        self.username = username 
        self.password = password
        self.is_logined = False

    def _encrypt_pw(self,password):
        hash_str = (self.username+password)
        hash_str = hash_str.encode("utf-8")
        return hashlib.sha256(hash_str).hexdigest()
        
    def checkpassword(self,password):
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password  