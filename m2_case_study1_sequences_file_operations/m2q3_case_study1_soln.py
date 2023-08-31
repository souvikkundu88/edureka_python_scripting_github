'''
Question 3
A website requires a user to input username and password to register. Write a program
to check the validity of password given by user. Following are the criteria for checking
password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
'''
import re

def check_password_validity(password):
    if 6 <= len(password) <= 12:
        if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"[0-9]", password) and re.search(r"[$#@]", password):
            return True
    return False

if __name__ == "__main__":
    user_password = input("Enter a password: ")
    
    if check_password_validity(user_password):
        print("Password is valid.")
    else:
        print("Password is not valid.")
