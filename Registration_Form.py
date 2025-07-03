import re

class Form:
    def __init__(self):
        self.stored_username = None
        self.stored_password = None
 
    def sign_up(self):
        username = str(input("Enter The Full Name : "))
        password = (input("Enter The Password : "))
        mo_no    =  int(input("Enter The Mo_No :"))
        email    = (input("Enter The E-mail : "))

        print("\n---------------------------------------")

        user_pattern = r'^[a-zA-Z_ ]+$'
        if re.match(user_pattern, username):
            print(username)
        else:
            print(f"{username}, is not match to policy")

        user_pass = r'^[a-z0-9A-Z._@!#$%]+$'
        if re.match(user_pass, password):
            print(password)
        else:
            print(f"{password}, is not match to policy")

        # user_mobile = r'^[0-9]{10}+$'
        # if re.match(user_mobile, mo_no ):
        #     print(mo_no)
        # else:
        #     print(f"{mo_no}, is not match to policy")

        print(mo_no)

        user_email = r'^[a-z0-9.@]+$'
        if re.match(user_email, email):
            print(email)
        else:
            print(f"{email}, is not match to policy")

        #Save Credentials.
        self.stored_username = username
        self.stored_password = password

        #print("Sign-up successfully!")
        print("---------------------------------------\n")

class Form_login(Form):
    def login(self, username, password):

        username = input("Enter the username : ")
        password = input("Enter the password : ")

        if username == self.stored_username and password == self.stored_password:
            print("Login Successfully\n")
            self.home()
        else: 
            print("Invalid Username and Password.....")
        print("---------------------------------------\n")

class Main_page(Form_login):
    def home(self):
        print("Welcome to my home page...........!")

register = Main_page()
register.sign_up()
register.login("usrname", "password")
