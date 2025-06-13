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
        json.dump(name, file)

#create another function to read the file
def readfile(fileName):
    with open(fileName+".json", "r") as file:
        testFile= json.load(file)
        print(testFile)

#Convert all dictionaries into a json file
writeFile(ducks, "ducks")
writeFile(kings, "kings")
writeFile(flames, "flames")
writeFile(spongebob, "spongebob")
writeFile(capitals, "capitals")

#create user interface
#ask user to login or sign up
signUp = str(input("do you want to login or sign up?   "))
signUp= signUp.lower().replace(" ", "")
signUp= signUp.find("signup")
print(signUp)

#allow user to sign up
if signUp != -1:
    username = str(input("Enter your username:   "))
    password = str(input("Enter your password:   "))
    UserLogin= {username: password}
    writeFile(UserLogin, "UserLogin")
    readfile("UserLogin")