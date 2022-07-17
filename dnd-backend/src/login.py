#!/usr/bin/env python3

import hashlib
from PyInquirer import prompt


login_prompt = [
        {
            'type': 'list',
            'name': "user_login_option",
            'message': "Sign Up or Login",
            'choices': ["Sign In", "Sign Up"]
        }
]

def login(login_selection):
    user_login = input("Enter username: ")
    user_hash = hashlib.md5(user_login.encode())
    if login_selection.get("user_login_option") == "Sign In":
        sign_in(user_hash)
    elif login_selection.get("user_login_option") == "Sign Up":
        sign_up(user_hash)

def user_dir_load():
    user_hash_dir = open("../resources/logins", "r+")
    user_hash_str = user_hash_dir.read()
    user_hash_vec = user_hash_str.split("\n")
    return user_hash_vec

def sign_in(user_hash):
    user_hash_vec = user_dir_load()
    print(user_hash_vec)

def sign_up(user_hash):
    user_hash_vec = user_dir_load()
    print(user_hash_vec)

def main():
    login_selection = prompt(login_prompt)
    login(login_selection)
    user_hash_dir.close()

if __name__ == "__main__":
    main()
