from getpass import *

def login():
    count = 0 
    while True: 
        userName = input("Hello! Welcome to Ebast app!, \n\nUsername: ") 
        password = getpass("Password: ")
        count += 1
        if count == 3: 
            #tells user bye
            break #exit
        else:
            if userName == 'Herman' and password == '2177':
                #let them in
                print("hello mr Herman , welcome back")
                break #they are in, exit loop
            else:
                print("sorry wrong password")

