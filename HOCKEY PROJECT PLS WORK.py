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
        "£_____": "Wheels",
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


"""
artists = {
    "lewiscapaldi": {
        "someoneyouloved.mp3": "Someone You Loved",
        "beforeyougo.mp3": "Before You Go",
        "holdmewhileyouwait.mp3": "Hold Me While You Wait",
        "foreveryougo.mp3": "Forever You Go",
        "lastgoodbye.mp3": "Last Goodbye"
    },
    "greenday": {
        "basketcase.mp3": "Basket Case",
        "americanidiot.mp3": "American Idiot",
        "goodriddance.mp3": "Good Riddance",
        "whenicomearound.mp3": "When I Come Around",
        "boulevardofbrokendreams.mp3": "Boulevard of Broken Dreams"
    },
    "foofighters": {
        "everlong.mp3": "Everlong",
        "wheels.mp3": "Wheels",
        "learntofly.mp3": "Learn to Fly",
        "monkeywrench.mp3": "Monkey Wrench",
        "bigme.mp3": "Big Me"
    },
    "shawnmendes": {
        "stitches.mp3": "Stitches",
        "inmyblood.mp3": "In My Blood",
        "senorita.mp3": "Senorita",
        "mercy.mp3": "Mercy",
        "lostinjapan.mp3": "Lost in Japan"
    },
    "metallica": {
        "nothingelsematters.mp3": "Nothing Else Matters",
        "entersandman.mp3": "Enter Sandman",
        "onebattery.mp3": "One Battery",
        "sadbuttrue.mp3": "Sad But True",
        "theunforgiven.mp3": "The Unforgiven"
    },
    "beatles": {
        "heyjude.mp3": "Hey Jude",
        "letme.mp3": "Let Me",
        "comein.mp3": "Come In",
        "youneveralone.mp3": "You Never Alone",
        "allivemadelove.mp3": "All I’ve Made Love"
    },
    "mozart": {
        "symphonyno40ingminor,k.550.mp3": "Symphony No. 40 in G minor, K. 550",
        "therequiem.mp3": "The Requiem",
        "einekleinenachtmusik.mp3": "Eine kleine Nachtmusik",
        "pianosonatano16incmajor,k.545.mp3": "Piano Sonata No. 16 in C major, K. 545",
        "dongiovanni.mp3": "Don Giovanni"
    },
    "arcticmonkeys": {
        "doiwannaknow?.mp3": "Do I Wanna Know?",
        "rumine?.mp3": "R U Mine?",
        "arabella.mp3": "Arabella",
        "cornerstone.mp3": "Cornerstone",
        "fluorescentadolescent.mp3": "Fluorescent Adolescent"
    }
}
"""