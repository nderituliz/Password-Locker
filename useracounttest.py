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

    def test_delete_user_account(self):

        self.new_account.save_user_details()
        test_newaccount = UserAccount("Gmail","User","Password")
        test_newaccount = save_user_details()
        self.new_account.delete_user_details()
        self.assertEqual(len(UserAccount.user_pass_list),1)

    def test_search_user_account(self):
        self.new_account.save_user_details()
        test_newaccount = UserAccount("Gmail","User","Password")
        test_newaccount = save_user_details()
        search_user = UserAccount.search_user_account("Facebook")
        self.assertEqual(search_user.account, test_newaccount.account)

    def test_account_exists(self):

        self.new_account.save_user_details()
        test_newaccount =UserAccount("Gmail","User","Password")
        test_newaccount.save_user_details()
        account_exists = UserAccount.check_user_account("Gmail")
        self.assertTrue(account_exists)

    def test_show_account_details(self):

        self.assertEqual(UserAccount.show_user_details(), UserAccount.user_pass_list)


    def test_copy_pwd(self):

        self.new_account.save_user_details()
        UserAccount.copy_pwd("password123")
        self.assertEqual(self.new_account.password, pyperclip.paste())

    
    

        

    
    