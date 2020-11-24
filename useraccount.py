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

    def save_user_details(self):

        UserAccount.user_pass_list.append(self)

    def delete_user_details(self):

        UserAccount.user_pass_list.remove(self)

    @classmethod
    def search_user_account(cls,account):

        for user_deets in cls.user_pass_list:
            if user_deets.account == account:
                return user_deets


    @classmethod
    def check_user_account(cls,account):
        """ check if a user account exists """

        for user_account_deets in cls.user_pass_list:
            if user_account_deets.account == account:
                return True
            return False

    
    @classmethod
    def show_user_details(cls):

        return cls.user_pass_list

    @classmethod
    def copy_pwd(cls,password):
        search_acc = UserAccount.search_user_account(password)
        pyperclip.copy(search_acc.password)
    


    

    