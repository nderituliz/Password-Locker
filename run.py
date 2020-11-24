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

def search_user(username):
    return User.search_user(username)

def create_user_details(account,email,password):

    new_account = UserAccount(account,email,password)
    return new_account

def save_user_credentials(user_cred):
    user_cred.save_user_details()

def show_account_credentials():
    return UserAccount.show_user_details()

def search_account(account):
    return UserAccount.search_user_account(account)


def delete_user_credentials(account):
    account.delete_user_details()


def main():
    print("/" * 30)
    print('\n')
    print("Welcome. Please enter your name: ")
    name = input()
    print("Hi" +" "+ f"{name}",+" "+"signup to continue")
    print("/"* 30)
    print('\n')
    print("Use the short codes as follows: 'su' to Sign Up, 'li' to Log In, 'ex' to Exit ")

    while True:
        short_code = input().lower()

        if short_code=='su':
            print("Create Account , by keying in your details")
            print("Username: ")
            username = input()
            print('\n')
            print("email")
            email = input()
            print("Password: ")
            password = input()

            save_user(create_useraccount(username,email,password))
            print('\n')
            print(f"{name}  Account Info:")
            print(f"username : {username} , email: {email} , password: {password}")
            print('\n')
            print(f"You have successfully created your account. Welcome {username}!")
            print ('\n')
            print ('\n')
            print("You can use these codes: 'ca' to Create a new Account, 'da' to Display Account, 'fa' to search Account, 'gp' to Generate a Password, 'ex' to exit")
            print ('\n')


        elif short_code == "ca":
            print("Enter your account details: ")
            print("Account Name: ")
            account = input()
            print("Email: ")
            email = input()

            print("Would you like us to generate a password for you?")
            if input()== "yes":
                letters = "any"
                how_many= len (letters)
                print("How long would you like your password to be? ")
                print(f"P.S: Maximum length of your password is {how_many}")
                lent = int(input())
                
                password = "" .join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)
                
                save_user_account_details(create_user_details(account, email, password))
                print("User Account Details saved! Enter 'da' to see your account")
                print ('\n')
                print ('\n')
                print ("Use the short code 'ca' to create a new account")
                print ('\n')
            elif input() == "no":
                print ("password: ")
                password = input()
                save_user_account_details(create_user_details(account, email, password))
                print ('\n')
                print("Use these short codes: 'ca' to create a new account")
                print ('\n')

                save_user(create_user_details(account, email, password))
                save_userCred(create_user_details(account, email, password))
                print('\n')
                print(f"New User {account} {email} created")
                print('\n')

            else:
                print("Your details were not capture, please use shortcode 'ca' and start again")

        elif short_code == "da":
            print(f"These are the credentials for {name}:")
            print ('\n')
            for user_deets in show_account_credentials():
                    print(f"{user_deets.account}\n {user_deets.email}\n {user_deets.password}")
            else: 
                print ('\n')
                print("You do not have any accounts saved")

        elif short_code == "fa":
                print("Please enter the name of the account your are searching for: ")
                search_useracc = input()
                if search_account(search_useracc):
                    search_acc = search_account(search_useracc)
                    print(f"{search_acc.account} {search_acc.email} {search_acc.password}")
                else: print("Account does not exist!")

        elif short_code == "gp":
                letters= "any"
                how_many = len(letters)
                print("How long would you like your password to be? ")
                print(f"P.S: Maximum length of your password is {how_many}")
                lent = int(input())
                password = "" .join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)

        elif short_code == "ex":
            print("logging out...")
            print ('\n')
            print("logged out")
            print ('\n')
            break

         else:
            print("Invalid inputs, please  use these short codes : 'ca' to create a new account, 'da' to display accounts, 'fa' to search an account, 'de' to delete account , 'gp' to generate a random password and 'ex' t0 logout")

if __name__=='__main__':
    main()