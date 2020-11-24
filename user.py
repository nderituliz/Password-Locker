class User:

    user_list = []

    def __init__(self, username, email, password):
        '''
        The purpose of this function to save user credentials
        '''
        self.username = username
        self.email = email
        self.password = password

     def save_user(self):
         """ 
         Save a user 
          """
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete a user 
        '''
        User.user_list.remove(self)

    @classmethod
    def search_user(cls, username):
        '''
        search a username 
        '''
        for user in cls.user_list:
            if user.username == username:
                return  user