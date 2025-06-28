import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
import json
import requests
import tempfile
import time
import random
import threading
import difflib

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
        "Enter Sandman": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Metallica_%20Enter%20Sandman%20Official%20Music%20Video.mp3",
        "For Whome the Bell Tolls": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/For%20Whom%20The%20Bell%20Tolls%20Remastered.mp3",
        "Sad But True": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Sad%20But%20True%20Remastered.mp3",
        "The Unforgiven": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/YouTube%20(1).mp3"
    },
    "Beatles": {
        "Hey Jude": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Hey%20Jude%20Remastered%202015.mp3",
        "Let It Be": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Let%20It%20Be%20Remastered%202009.mp3",
        "Here Comes The Sun": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/The%20Beatles%20-%20Here%20Comes%20The%20Sun%202019%20Mix.mp3",
        "Day Tripper": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Day%20Tripper%20Remastered%202015.mp3",
        "Yellow Submarine": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/The%20Beatles%20-%20Yellow%20Submarine.mp3"
    },
    "Beethoven": {
        "Symphony No. 5 in C Minor, Op. 67": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Beethoven_%20Symphony%20no%205%20in%20C%20minor%20op67.mp3",
        "Für Elise": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Beethoven%20-%20Fr%20Elise%20Piano%20Version.mp3",
        "Moonlight Sonata": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Beethoven%20-%20Moonlight%20Sonata%20FULL.mp3",
        "Ode to Joy": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Ode%20to%20Joy.mp3",
        "Turkish March, from The Ruins of Athens": "https://raw.githubusercontent.com/pbalalas/Audio-Python/main/Ludwig%20van%20Beethoven%20-%20Turkish%20March%20from%20_The%20Ruins%20of%20Athens_%20piano%20solo%20version.mp3"
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

#create funciton to accept close matches
def closeMatch(input, actual, threshold = 0.8):
    def normalize(text):
        text = text.lower()
        allowed = set("abcdefghijklmnopqrstuvwxyz0123456789")
        text = "".join(char for char in text if char in allowed)
        text = text.split()
        text = "".join(word for word in text if word not in ("and", "an", "the"))
        return text
    input = normalize(input)
    actual = normalize(actual)
    similarity = difflib.SequenceMatcher(None, input, actual).ratio()
    return similarity >= threshold

#allow user to sign up, using a function
def signUp():    
    #creates a new file, if file is corrupted or missing
    try:
        userLogin = readFile("userLogin")
    except(FileNotFoundError, json.JSONDecodeError):
        userLogin= {}
    
    print("You are signing up")
    username = str(input("Enter your username:   ").strip())

    while username in userLogin:
        print("username already exists")
        username = str(input("Enter your username(or type 'login' to login instead):   ").strip())
        if closeMatch(username, "login") == True:
            return "login"
        
    password = str(input("Enter your password:   ").strip())
    doubleChecking = str(input("retype your password:  ").strip())
    while doubleChecking != password: 
        if doubleChecking != password:
            print("password does not match, retry")
            password = str(input("Enter your password:   ").strip())
            doubleChecking = str(input("retype your password:   ").strip())
        
    userLogin[username] = {"password": password, "score": 0}
    writeFile(userLogin, "userLogin")
    return "successful", username


#allow the user to login to their account
def login():
    try:
        userLogin = readFile("userLogin")
    except(FileNotFoundError, json.JSONDecodeError):
        userLogin= {}
    
    print("You are logging in")
    username = str(input("enter your username:   ").strip())
    
    while username not in userLogin:
        username = str(input("username does not exist, try again (or type 'signup' to signup instead):   ").strip())
        if closeMatch(username, "signup") == True:
            return "signup"
    
    password = str(input("enter your password:   ").strip())
    if userLogin[username]["password"] == password:
        print("login successful")
        return "successful", username
    else:
        while userLogin[username]["password"] != password:
            password = str(input("password is incorrect, try again:   ").strip())
        print("login successful")
        return "successful", username
    
#create user interface
#ask user to login or sign up
login_flag = False
signUp_flag = False
while login_flag == False and signUp_flag == False:
    access = str(input("do you want to login or sign up?:   "))
    signUp_flag = closeMatch(access, "signup")
    login_flag= closeMatch(access, "login")

#implement sign up and login actions
while True:
    if signUp_flag != False:
        result, username = signUp()
        if result == "login":
            signUp_flag = False
            login_flag = True
        elif result == "successful":
            break
    elif login_flag != False:
        result, username = login()
        if result == "signup":
            signUp_flag = True
            login_flag = False
        elif result == "successful":
            userLogin = readFile("userLogin")
            print("\nYour total score is ", userLogin[username]["score"])
            break

#create function to choose a random url from the dictionary
def randomSong():
    #chooses a random artist from the dictionary artists
    artists= readFile("artists")
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
    if duration > 0:
        try:
            #this part should stop as soon as the user enters something
            pygame.mixer.init()
            pygame.mixer.music.load(tempPath)
            pygame.mixer.music.play()

            stop_flag = threading.Event()
            guess = {"guess": ""}
            
            def wait_for_input():
                guess["guess"] = input("Enter your guess:   ")
                stop_flag.set()

            inputThread = threading.Thread(target = wait_for_input)
            inputThread.start()
            
            stop_flag.wait(duration)
            
            pygame.mixer.music.fadeout(2000)
            time.sleep(2)
            inputThread.join()
            pygame.mixer.quit()
            os.remove(tempPath)

            return guess["guess"]
            
        except Exception as e:
            print(f"there was an error:   {e}")
            
    else:
        try:
            #this part the music should stop after a delay, or when the user enters something
            pygame.mixer.init()
            pygame.mixer.music.load(tempPath)
            pygame.mixer.music.play()

            input("press enter to stop playing music")
                
            pygame.mixer.music.fadeout(2000)
            time.sleep(2)
            pygame.mixer.quit()
            os.remove(tempPath)

        except Exception as e:
            print(f"there was an error:   {e}")

#start creating UI to guess the song
def pgame(again = "", kill = ""):
    while True: 
        if again == " again":
            while True:
                listen = input("Do you want to listen to the whole song:   ")
                if closeMatch(listen, "yes"):
                    return "listen"
                elif closeMatch(listen, "no"):
                    break
                else:
                    print("please type yes or no")
                    
        play_game = input(f"Do you want to play{again}?:   ")
        if closeMatch(play_game, "yes"):
            play_game = True
            break
        elif kill == "kill":
            if closeMatch(play_game, "no") == True:
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
        elif kill == "":
            if closeMatch(play_game, "no") == True:
                play_game = False
                break
        else:
            print("please type yes or no")
    return  play_game
#just testing: playAudio(artists["Greenday"]["American Idiot"], 5)


#create a function to change the song name name into one with only the first letters
def blank(songName):
    letters= []
    for letter in songName:
        if letter == " ":
            letters.append(" ")
        elif letter == letter.lower():
            letters.append("_")
        else:
            letters.append(letter)
    masked = "".join(letters)
    return masked    



#actually allow the user to play the game

play_game = True
play_game= pgame("", "kill")

while play_game == True:
    name, songName = randomSong()
    guess = playAudio(artists[name][songName], 5)
    #three points for getting the answer first try
    if closeMatch(guess, songName)== True:
        userLogin = readFile("userLogin")
        userLogin[username]["score"] += 3
        writeFile(userLogin, "userLogin")
        print("you get 3 points for getting it first try")
        print("your total score is ",userLogin[username]["score"], " points")
        play_game = pgame(" again")
        if play_game == "listen":
                playAudio(artists[name][songName], 0)
    else:
        #gives a clue (the artist name) and gives two points for getting it second try
        print("The name of the artist is:")
        print(name)
        guess = playAudio(artists[name][songName], 7)
        
        if closeMatch(guess, songName)== True:
            userLogin = readFile("userLogin")
            userLogin[username]["score"] += 2
            writeFile(userLogin, "userLogin")
            print("you get 2 points for getting it second try")
            print("your total score is",userLogin[username]["score"])
            play_game = pgame(" again")
            if play_game == "listen":
                playAudio(artists[name][songName], 0)
        
        else:
            #gives a final clue (song name but blanked) and gives 1 point for getting it right third try
            masked = blank(songName)
            print("Here is the song name but blanked:")
            print(masked)
            guess = playAudio(artists[name][songName], 10)

            if closeMatch(guess, songName)== True:
                userLogin = readFile("userLogin")
                userLogin[username]["score"] += 1
                writeFile(userLogin, "userLogin")
                print("you get 1 point for getting it on your last try")
                print("your total score is ",userLogin[username]["score"])
                play_game = pgame(" again")
                if play_game == "listen":
                    playAudio(artists[name][songName], 0)
            else:
                #gets angry at you for loosing
                print("You used up all your guesses- 0 points")
                print("YOU FAILED")
                print(f"the correct answer was {songName} by {name} \n")
                play_game = pgame(" again")
                if play_game == "listen":
                    playAudio(artists[name][songName], 0)


while True: 
        leaderboard = input("Do you want to see the leaderboard?:   ")
        if closeMatch(leaderboard, "yes"):
            break
        elif closeMatch(leaderboard, "no"):
            print("Thank you for playing")
            exit()
        else:
            print("please type yes or no")

userLogin = readFile("userLogin")
sortedScore = sorted(userLogin.items(), key = lambda x: x[1]["score"], reverse = True)
leaderboard = sortedScore[0:5]

print("Here is the leaderboard:\n")
for rank, (user, data) in enumerate(leaderboard, start =1):
    print(f"#{rank} {user}: {data['score']} points")

print("\nThank you for playing")
time.sleep(10)
exit()