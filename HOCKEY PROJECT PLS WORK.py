import json
import pygame
import requests
import tempfile
import time
import random

#Create dictionaries to store the musicians in multiple json files
artists = {
    "Lewis Capaldi": {
        "Someone You Loved": "someoneyouloved.mp3",
        "Before You Go": "beforeyougo.mp3",
        "Hold Me While You Wait": "holdmewhileyouwait.mp3",
        "Forever You Go": "foreveryougo.mp3",
        "Last Goodbye": "lastgoodbye.mp3"
    },
    "Greenday": {
        "Basket Case": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Basket%20Case.mp3",
        "American Idiot": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Green%20Day%20-%20American%20Idiot%20Official%20Audio%20(1).mp3",
        "Good Riddance": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Green%20Day%20-%20Good%20Riddance%20Time%20of%20Your%20Life%20Official%20Music%20Video%204K%20UPGRADE.mp3",
        "When I Come Around": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/When%20I%20Come%20Around.mp3",
        "Boulevard of Broken Dreams": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Green%20Day%20-%20Boulevard%20of%20Broken%20Dreams%20Official%20Audio.mp3"
    },
    "Foo Fighters": {
        "Everlong": "everlong.mp3",
        "Wheels": "wheels.mp3",
        "Learn to Fly": "learntofly.mp3",
        "Monkey Wrench": "monkeywrench.mp3",
        "Big Me": "bigme.mp3"
    },
    "Shawn Mendes": {
        "Stitches": "stitches.mp3",
        "In My Blood": "inmyblood.mp3",
        "Senorita": "senorita.mp3",
        "Mercy": "mercy.mp3",
        "Lost in Japan": "lostinjapan.mp3"
    },
    "Metallica": {
        "Nothing Else Matters": "nothingelsematters.mp3",
        "Enter Sandman": "entersandman.mp3",
        "One Battery": "onebattery.mp3",
        "Sad But True": "sadbuttrue.mp3",
        "The Unforgiven": "theunforgiven.mp3"
    },
    "Beatles": {
        "Hey Jude": "heyjude.mp3",
        "Let Me": "letme.mp3",
        "Come In": "comein.mp3",
        "You Never Alone": "youneveralone.mp3",
        "All I’ve Made Love": "allivemadelove.mp3"
    },
    "Mozart": {
        "Symphony No. 40 in G minor, K. 550": "symphonyno40ingminor,k.550.mp3",
        "The Requiem": "therequiem.mp3",
        "Eine kleine Nachtmusik": "einekleinenachtmusik.mp3",
        "Piano Sonata No. 16 in C major, K. 545": "pianosonatano16incmajor,k.545.mp3",
        "Don Giovanni": "dongiovanni.mp3"
    },
    "Arctic Monkeys": {
        "Do I Wanna Know?": "doiwannaknow?.mp3",
        "R U Mine?": "rumine?.mp3",
        "Arabella": "arabella.mp3",
        "Cornerstone": "cornerstone.mp3",
        "Fluorescent Adolescent": "fluorescentadolescent.mp3"
    },
    "Bach": {
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
        return "successful", username
    else:
        while userLogin[username]["password"] != password:
            password = str(input("password is incorrect, try again:   "))
        print("login successful")
        return "successful", username
    
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
        result, username = login()
        if result == "signup":
            signUp_flag = 0
            login_flag = -1
        elif result == "successful":
            userLogin = readFile("userLogin")
            print("\nYour score is ", userLogin[username]["score"])
            break

#create function to choose a random url from the dictionary
def randomSong():
    #chooses a random artist from the dictionary artists
    name = random.choice(list(artists.keys()))
    #chooses a random song from the artist
    songName = random.choice(list(artists[name]))
    return name, songName

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

#start creating UI to guess the song
while True: 
    play_game = input("Do you want to play?   ")
    if play_game.lower().replace(" ","").find("yes") != -1:
        break
    elif play_game.lower().replace(" ", "").find("no") != -1:
        print("why did you even login??")
        time.sleep(2)
        print("what is the point?!?")
        time.sleep(2)
        print("what a waste of time!!!!!")
        time.sleep(2)
        print("The AMouNt OF FlESh and Bone ThaT wEnT inTo ThiS!!")
        time.sleep(2)
        print("YOU WILL REGRET THIS")
        time.sleep(3)
        print("goodbye")
        exit()
    else:
        print("please type yes or no")
        
print("hello?")