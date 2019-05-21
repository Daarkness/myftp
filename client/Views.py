class View:
    def get_cmd(self):
        input_msg = input("please input your cmd:")
        return input_msg

    def display(self):
        print("========================")
        print("====  welcome to ftp====")
        print("========================")
    def get_user_msg(self):
        username = input("Please input your username:") 
        password =  input("Please input your Password:") 
        return username,password 

    

                                                                                                                             