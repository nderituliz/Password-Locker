import pyperclip
class UserAccount:
    """ 
    class that creates instances of users accounts
     """
    user_pass_list = []

    def __init__(self,account,email,password):
        self.account = account
        self.email= email
        self.password = password

   