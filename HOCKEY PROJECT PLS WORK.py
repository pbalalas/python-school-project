import json
import pygame
import requests
import tempfile
import time
import random

#Create dictionaries to store the musicians in multiple json files
artists = {
    "Lewis Capaldi": {
        "Someone You Loved": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Lewis%20Capaldi%20-%20Someone%20You%20Loved.mp3",
        "Before You Go": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Lewis%20Capaldi%20-%20Before%20You%20Go%20Official%20Video.mp3",
        "Hold Me While You Wait": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Lewis%20Capaldi%20-%20Hold%20Me%20While%20You%20Wait%20Interlude%20Session.mp3",
        "Forever": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Forever.mp3",
        "Bruises": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Lewis%20Capaldi%20-%20Bruises%20Official%20Audio.mp3"
    },
    "Greenday": {
        "Basket Case": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Basket%20Case.mp3",
        "American Idiot": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Green%20Day%20-%20American%20Idiot%20Official%20Audio%20(1).mp3",
        "Good Riddance": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Green%20Day%20-%20Good%20Riddance%20Time%20of%20Your%20Life%20Official%20Music%20Video%204K%20UPGRADE.mp3",
        "When I Come Around": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/When%20I%20Come%20Around.mp3",
        "Boulevard of Broken Dreams": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Green%20Day%20-%20Boulevard%20of%20Broken%20Dreams%20Official%20Audio.mp3"
    },
    "Foo Fighters": {
        "Everlong": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Foo%20Fighters%20-%20Everlong%20Official%20HD%20Video.mp3",
        "Wheels": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Wheels.mp3",
        "Learn to Fly": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Foo%20Fighters%20-%20Learn%20to%20Fly.mp3",
        "Monkey Wrench": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Foo%20Fighters%20-%20Monkey%20Wrench.mp3",
        "Pretender": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Foo%20Fighters%20-%20The%20Pretender.mp3"
    },
    "Metallica": {
        "Nothing Else Matters": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Metallica_%20Nothing%20Else%20Matters%20Official%20Music%20Video.mp3",
        "Enter Sandman": "entersandman.mp3",
        "For Whome the Bell Tolls": "forwhomethebelltolls.mp3",
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
    "Beethoven": {
        "Symphony No. 5 in C Minor, Op. 67": "symphony5incminorop67.mp3",
        "Für Elise": "furelise.mp3",
        "Moonlight Sonata": "moonlightsonata.mp3",
        "Ode to Joy": "odetojoy.mp3",
        "Piano Concerto No. 5 in E-flat major, Op. 73": "pianoconcerto5.mp3"
    },
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