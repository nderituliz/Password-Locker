import unittest
from user import User 

class UserTest(unittest.TestCase):

    def setUpClass(self):
        self.new_user = User("nderituliz", "nderituliz@gmail.com", "password123")

    def tearDown(self):

        User.user_list = []

    def test__init(self):
        self.assertEqual(self.new_user.username , "nderituliz")
        self.assertEqual(self.new_user.email,"nderituliz@gmail.com")
        self.assertEqual(self.new_user.password,"password123")

    def test_save_user(self):

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def test_save_multiple_users(self):

        self.new_user.save_user()
        test_user = User("test", "nderituliz@gmail.com", "password123")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):

        self.new_user.save_user()
        test_user = User("test", "nderituliz@gmail.com", "password123")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_search_user(self):

        self.new_user.save_user()
        test_user = User("test", "nderituliz@gmail.com", "password123")
        test_user.save_user()
        user_found = User.search_user("nderituliz")
        self.assertEqual(user_found.username, self.new_user.username)


if __name__ = '__main__':
    unittest.main()