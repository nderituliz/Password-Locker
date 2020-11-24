from useraccount import UserAccount 
from user import User
import random

def create_useraccount(username,email,password):

    new_user = User(username,email,password)
    return new_user

def save_user(user):

    user.save_user()


def save_user_account_details(user_details):
    user_details.save_user_account_details

