import json

#Create dictionaries to store the musicians in multiple json files
artists = {
    "lewiscapaldi": {
        "S_______ Y__ L____": "Someone You Loved",
        "B_____ Y__ G__": "Before You Go",
        "H___ M_ W____ Y__ W___": "Hold Me While You Wait",
        "F______ Y__ G__": "Forever You Go",
        "L___ G______": "Last Goodbye"
    },
    "greenday": {
        "B______ C___": "Basket Case",
        "A_______ I____": "American Idiot",
        "G___ R_______": "Good Riddance",
        "W___ I C___ A_____": "When I Come Around",
        "B_________ __ B_____ D______": "Boulevard of Broken Dreams"
    },
    "foofighters": {
        "E____": "Everlong",
        "T___ C__ D___": "The Color Dave",
        "L___ C__": "Learn to Fly",
        "M__ W___": "Monkey Wrench",
        "B__ M___ B__": "Big Me"
    },
    "shawnmendes": {
        "S_________": "Stitches",
        "I_ T___ Y__": "In My Blood",
        "S____ S___": "Senorita",
        "M__ I_ Y__": "Mercy",
        "L____ M_": "Lost in Japan"
    },
    "metallica": {
        "N_______": "Nothing Else Matters",
        "E_______": "Enter Sandman",
        "O___ B____": "One Battery",
        "S___ M_____": "Sad But True",
        "T__ U_________": "The Unforgiven"
    },
    "beatles": {
        "H__ J___ B____": "Hey Jude",
        "L___ M_": "Let Me",
        "C___ I_": "Come In",
        "Y__ N__ A__": "You Never Alone",
        "A__ I_ M___ L___": "All I’ve Made Love"
    },
    "mozart": {
        "S____ K. 525": "Symphony No. 40 in G minor, K. 550",
        "T__ R______": "The Requiem",
        "F____ C______": "Eine kleine Nachtmusik",
        "P______ K. 545": "Piano Sonata No. 16 in C major, K. 545",
        "D___ C_______": "Don Giovanni"
    },
    "arcticmonkeys": {
        "D___ S_____": "Do I Wanna Know?",
        "R______ W___": "R U Mine?",
        "A_____": "Arabella",
        "C_____ M__": "Cornerstone",
        "F__ C______": "Fluorescent Adolescent"
    }
}



#create a function to write dictionaries into json file
#will also help with user logins later on
def writeFile(name, fileName):
    with open(fileName+".json", "w") as file:
        json.dump(name, file, indent=4)

#create another function to read the file
def readFile(fileName):
    with open(fileName+".json", "r") as file:
        testFile= json.load(file)
        return testFile

#Convert all dictionaries into a json file
writeFile(artists, "artists")

#allow user to sign up, using a function
def signUp():    
    #creates a new file, if file is corrupted or missing
    try:
        userLogin = readFile("userLogin")
    except(FileNotFoundError, json.JSONDecodeError):
        userLogin= {}
    
    print("You are signing in")
    username = str(input("Enter your username:   "))

    while username in userLogin:
        print("username already exists")
        username = str(input("Enter your username(or type 'login' to login instead):   "))
        if username.lower().replace(" ", "").find("login") != -1:
            return "login"
        
    password = str(input("Enter your password:   "))
    doubleChecking = str(input("retype your password:  "))
    while doubleChecking != password: 
        if doubleChecking != password:
            print("password does not match, retry")
            password = str(input("Enter your password:   "))
            doubleChecking = str(input("retype your password:   "))
        
    userLogin[username] = {"password": password, "score": 0}
    writeFile(userLogin, "userLogin")
    return "successful"


#allow the user to login to their account
def login():
    try:
        userLogin = readFile("userLogin")
    except(FileNotFoundError, json.JSONDecodeError):
        userLogin= {}
    
    print("You are logging in")
    username = str(input("enter your username:   "))
    
    while username not in userLogin:
        username = str(input("username does not exist, try again (or type 'signup' to signup instead):   "))
        if username.lower().replace(" ", "").find("signup") != -1:
            return "signup"
    
    password = str(input("enter your password:   "))
    if userLogin[username]["password"] == password:
        print("login successful")
        return "successful"
    else:
        while userLogin[username]["password"] != password:
            password = str(input("password is incorrect, try again:   "))
        print("login successful")
        return "successful"
    
#create user interface
#ask user to login or sign up
signUp_flag = -1
login_flag = -1
while login_flag == -1 and signUp_flag == -1:
    access = str(input("do you want to login or sign up?   "))
    access= access.lower().replace(" ", "")
    signUp_flag= access.find("signup")
    login_flag= access.find("login")

#implement sign up and login actions
while True:
    if signUp_flag != -1:
        result = signUp()
        if result == "login":
            signUp_flag = -1
            login_flag = 0
        elif result == "successful":
            break
    elif login_flag != -1:
        result = login()
        if result == "signup":
            signUp_flag = 0
            login_flag = -1
        elif result == "successful":
            break

#Create the random number generator to take random artist
import random
