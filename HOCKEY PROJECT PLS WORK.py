import json

#Create dictionaries for teams to store in a json file
ducks= {"Leo Carlson": 9,
        "Robby Fabri": 7,
        "Cutter Gauthier": 6,
        "Jansen Harkins": 6,
        "Ross Jhonson": 4,
        "Goalkeeper": 3}

kings= {"Quintin Byfield": 5,
        "Philip Denault": 2,
        "Kevin Fiala": 2,
        "Trevor Lewis": 6,
        "Taylor Ward": 10,
        "Goalkeeper": 7}

flames= {"Morgan Frost": 10,
         "Kevin Rooney": 10,
         "Conner Zairy": 10,
         "Ryan Lomberg": 1,
         "Jake Bean": 1,
         "Goalkeeper": 2}

spongebob= {"SpongeBob": 1,
            "Patrick": 1,
            "Sandy": 1,
            "Crabby Patty": 1,
            "Squidward": 1,
            "Goalkeeper": 7}

capitals= {"Nickolas Backstrom": 7,
           "Dylen Strom": 6,
           "Ethen Frank": 5,
           "Ryon Leonard": 4,
           "Jhon Carlson": 3,
           "Goalkeeper": 7}

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
writeFile(ducks, "ducks")
writeFile(kings, "kings")
writeFile(flames, "flames")
writeFile(spongebob, "spongebob")
writeFile(capitals, "capitals")

#allow user to sign up
def signUp():    
    try:
        userLogin = readFile("userLogin")
    except(FileNotFoundError, json.JSONDecodeError):
        userLogin= {}
    
    username = str(input("Enter your username:   "))

    while username in userLogin:
        print("username already exists")
        username = str(input("Enter your username(or type 'login' to login instead):   "))
        if username.lower().replace(" ", "").find("login") != -1:
            login_flag = username
            return login_flag
        
    password = str(input("Enter your password:   "))
    doubleChecking = str(input("retype your password:   "))
    while doubleChecking != password: 
        if doubleChecking != password:
            print("password does not match, retry")
            password = str(input("Enter your password:   "))
            doubleChecking = str(input("retype your password:   "))
        
    userLogin[username] = {"password": password, "score": 0}
    writeFile(userLogin, "userLogin")
    return "success"


#allow the user to login to their account
def login():
    try:
        userLogin = readFile("userLogin")
    except(FileNotFoundError, json.JSONDecodeError):
        userLogin= {}
    
    username = str(input("enter your username"))
    
    while username not in userLogin:
        username = str(input("username does not exist, try again (or type 'signup' to signup instead):   "))
        if username.lower().replace(" ", "").find("signup") != -1:
            signUp_flag = username
            return signUp_flag
    
    password = str(input("enter your password:   "))
    if userLogin[username]["password"] == password:
        print("login successful")
    else:
        while userLogin[username]["password"] != password:
            password = str(input("password is incorrect, try again:   "))
        print("login successful")
        return "success"
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
        if result != -1:
            login()
        else:
            break
    elif login_flag != -1:
        result = login()
        if result != -1:
            signUp()
        else:
            break


