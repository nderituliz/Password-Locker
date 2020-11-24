import unittest
from useraccount import UserAccount
import pyperclip

class UserAccountTest(unittest.TestCase):

    def setUp(self):
        self.new_account = UserAccount("Gmail", "nderituliz@gmail.com", "password123")
    
    def tearDown(self):
        UserAccount.user_pass_list = []

    def test_init(self):

        self.assertEqual(self.new_account.account,"Gmail")
        self.assertEqual(self.new_account.email,"ndertuliz@gmail.com")
        self.assertEqual(sel.new_account.password,"password123")

    def test_save_user(self):

        self.new_account.save_user_details()
        self.assertEqual(len(UserAccount.user_pass_list),1)

    def test_saving_multiple_accounts(self):

        self.new_account.save_user_details()
        test_newaccount = UserAccount("Gmail","User","Password")
        test_newaccount.save_user_details()
        self.assertEqual(len(UserAccount.user_pass_list),2)

    