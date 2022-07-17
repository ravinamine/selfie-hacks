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
    user_hash = user_hash.hexdigest()
    if login_selection.get("user_login_option") == "Sign In":
        sign_in(user_hash, user_login)
    elif login_selection.get("user_login_option") == "Sign Up":
        sign_up(user_hash, user_login)

def user_dir_load():
    user_hash_dir = open("../resources/logins", "r")
    user_hash_str = user_hash_dir.read()
    user_hash_vec = user_hash_str.split("\n")
    user_hash_dir.close()
    return user_hash_vec

def sign_in(user_hash, user_login):
    user_hash_dir = open("../resources/logins", "a")
    user_hash_vec = user_dir_load()
    for x in user_hash_vec:
        if user_hash == x:
            print("Welcome " + user_login)
            return
    print("User not found, please sign up")
    user_hash_dir.close()
    return

def sign_up(user_hash, user_login):
    user_hash_dir = open("../resources/logins", "a")
    user_hash_vec = user_dir_load()
    for x in user_hash_vec:
        if x == user_hash:
            print("User already exists, please log in")
            return
    user_hash_dir.write(user_hash + "\n")
    print("Successfully created user, welcome!")
    user_hash_dir.close()
    return

def main():
    login_selection = prompt(login_prompt)
    login(login_selection)

if __name__ == "__main__":
    main()
