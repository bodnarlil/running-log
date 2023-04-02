# Lilia Bodnar
# Demo running log login screen
# log in, add user, change password, view users

import sqlite3

# connect to the database...
sqliteConnectionRunningLog = sqlite3.connect('runningLog.db')

# cursor
cursor = sqliteConnectionRunningLog.cursor()

# print statement will execute if there are no errors
print("Connected to the database")
print("")

# close the connection
sqliteConnectionRunningLog.close()

# done with database stuff

# hold the users and their passwords
credentials = {}

def newUser():
    # username in the format firstnamelastname and password is whatever they make it
    firstName = input("enter your first name: ").lower()
    lastName = input("enter your last name: ").lower()

    username = firstName+lastName
    password = input("enter your desired password: ") # keep the user's cases (no lower or upper)

    if(username in credentials):
        print("")
        print("username already in use")
        print("")
        return ""
    
    print("")
    print("your username is",username)
    print("your password is",password)
    print("")
    save = input("is this your correct password? y/n: ").lower()
    while(save != "y" and save != "n"): # stupid error here supposed to run until user enters y or n
        save = input("please enter y if "+password+" is your correct password or n if it is not: ").lower()
    if(save == "y"):
        credentials[username] = password
    elif(save == "n"):
            password = input("please enter your desired password: ")
            print("your password is",password)
            save = input("is this your correct password? y/n: ").lower()
            while(save != "y" and save != "n"):
                save = input("please enter y if",password,"password is your correct password or n if it is not: ").lower()
            credentials[username] = password # this will run once the user says yes, their password is correct 
    else:
        print("error. please restart the program") # this should never run
    print("")

def logIn():
    username = input("enter your username: ")
    password = input("enter your password: ")
    for key, item in credentials.items():
        if(username == key and password == item):
            print("you have succesfully logged in")
            print("welcome,",username)
            print("")
            return username
    print("you could not log in with those credentials. please try again or choose another option")
    print("")
    return "you could not log in with those credentials. please try again or choose another option"

# view all the users and their passwords
def viewUsers():
    if(len(credentials) == 0): # check to see if the dictionary is empty
        print("no users have been entered")
    for key, item in credentials.items():
        print("username:",key,"| password:",item)

# change password
def changePassword():
    username = input("enter your username: ")
    password = input("enter your current password: ")
    for item, key in credentials.items():
        if(item == username and password == key):
            newPassword = input("account located. please enter your new password: ")
            credentials[username] = newPassword
            print("password succesfully updated")
            return username
    print("your username and password combination are incorrect. try again or choose another option")
    return username

# run the program below

def runningLog():
    choice = "nada"
    print("welcome to the demo of the logging in feature.")
    print("")

    while (choice != "exit"):
        print("---")
        print("")
        print("(a) add a new user")
        print("(b) log in as an existing user")
        print("(c) view all users and passwords")
        print("(d) change account password")
        print("")
        choice = input("enter an option: ").lower()
        if(choice == "a"):
            newUser()
        elif(choice == "b"):
            logIn()
        elif(choice == "c"):
            viewUsers()
        elif(choice == "d"):
            changePassword()
        elif(choice == "exit"):
            print("terminating program...")
            break
        else:
            print("please try again. add user (a), log in (b), or end the program (exit)")

# test dictionary
def testDictionary():
    test = {}

    test["testItem"] = "testKey"

    test[0] = 1

    number = 0
    for item, key in test.items():
        number+=1
        print("set number",number)
        print("item:",item)
        print("key:",key)
        print("")

testDictionary()

runningLog