import unittest
from user import User 

class UserTest(unittest.TestCase):

    def setUpClass(self):
        self.new_user = User("nderituliz", "nderituliz@gmail.com", "password123")

    def tearDown(self):

        User.user_list = []

    