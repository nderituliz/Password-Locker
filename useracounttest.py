import unittest
from useraccount import UserAccount
import pyperclip

class UserAccountTest(unittest.TestCase):

    def setUp(self):
        self.new_account = UserAccount("Gmail", "nderituliz@gmail.com", "password123")
    
    def tearDown(self):
        UserAccount.user_pass_list = []

    