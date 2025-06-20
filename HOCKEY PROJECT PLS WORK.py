import json
import pygame
import requests
import tempfile
import time
import random

#Create dictionaries to store the musicians in multiple json files
artists = {
    "lewiscapaldi": {
        "Someone You Loved": "someoneyouloved.mp3",
        "Before You Go": "beforeyougo.mp3",
        "Hold Me While You Wait": "holdmewhileyouwait.mp3",
        "Forever You Go": "foreveryougo.mp3",
        "Last Goodbye": "lastgoodbye.mp3"
    },
    "greenday": {
        "Basket Case": "basketcase.mp3",
        "American Idiot": "americanidiot.mp3",
        "Good Riddance": "goodriddance.mp3",
        "When I Come Around": "whenicomearound.mp3",
        "Boulevard of Broken Dreams": "boulevardofbrokendreams.mp3"
    },
    "foofighters": {
        "Everlong": "everlong.mp3",
        "Wheels": "wheels.mp3",
        "Learn to Fly": "learntofly.mp3",
        "Monkey Wrench": "monkeywrench.mp3",
        "Big Me": "bigme.mp3"
    },
    "shawnmendes": {
        "Stitches": "stitches.mp3",
        "In My Blood": "inmyblood.mp3",
        "Senorita": "senorita.mp3",
        "Mercy": "mercy.mp3",
        "Lost in Japan": "lostinjapan.mp3"
    },
    "metallica": {
        "Nothing Else Matters": "nothingelsematters.mp3",
        "Enter Sandman": "entersandman.mp3",
        "One Battery": "onebattery.mp3",
        "Sad But True": "sadbuttrue.mp3",
        "The Unforgiven": "theunforgiven.mp3"
    },
    "beatles": {
        "Hey Jude": "heyjude.mp3",
        "Let Me": "letme.mp3",
        "Come In": "comein.mp3",
        "You Never Alone": "youneveralone.mp3",
        "All I’ve Made Love": "allivemadelove.mp3"
    },
    "mozart": {
        "Symphony No. 40 in G minor, K. 550": "symphonyno40ingminor,k.550.mp3",
        "The Requiem": "therequiem.mp3",
        "Eine kleine Nachtmusik": "einekleinenachtmusik.mp3",
        "Piano Sonata No. 16 in C major, K. 545": "pianosonatano16incmajor,k.545.mp3",
        "Don Giovanni": "dongiovanni.mp3"
    },
    "arcticmonkeys": {
        "Do I Wanna Know?": "doiwannaknow?.mp3",
        "R U Mine?": "rumine?.mp3",
        "Arabella": "arabella.mp3",
        "Cornerstone": "cornerstone.mp3",
        "Fluorescent Adolescent": "fluorescentadolescent.mp3"
    },
    "bach": {
        "Toccata and Fugue in D minor, BWV 565": "toccataandfugue.mp3",
        "Brandenburg Concerto No. 3": "brandenburgconcerto.mp3",
        "Air on the G String": "aironagstring.mp3",
        "Goldberg Variations": "goldbergvariations.mp3",
        "The Well-Tempered Clavier": "welltemperedclavier.mp3"
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

#create function to choose a random url from the dictionary
def randomSong():
    #chooses a random artist from the dictionary artists
    name = random.choice(list(artists.keys()))
    #chooses a random song from the artist
    song = random.choice(list(artists[name].keys()))
    return name, song

#create another function to download the youtube url as audio
def playAudio(url, duration):    
    # Download the audio file temporarily
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch audio.")
        return
    
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as file:
        file.write(response.content)
        tempPath = file.name
            
    #play audio for requested amount of time
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(tempPath)
        pygame.mixer.music.play()
        time.sleep(duration)
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except Exception as e:
        print("there was an error:   {e}")

playAudio("https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Green%20Day%20-%20American%20Idiot%20Official%20Audio%20(1).mp3", 5)
