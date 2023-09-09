import webbrowser
import os
import sys
import datetime
import wikipedia
import speedtest
import pyautogui
import cv2
import random
from twilio.rest import Client
import instaloader
import PyPDF2
from pywikihow  import search_wikihow
import requests
import twilio
from bs4 import BeautifulSoup
import wolframalpha
import openai
import openai 
from requests.exceptions import ConnectionError
from googlesearch import search
import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import psutil

# Initialize OpenAI GPT-3
api_key = "YOUR_OPENAI_API_KEY"
openai.api_key = api_key

# Initialize Wolfram Alpha API
wolfram_alpha_app_id = "YOUR_WOLFRAM_ALPHA_APP_ID"
wolfram_alpha_client = wolframalpha.Client(wolfram_alpha_app_id)

# Initialize Wikipedia
wikipedia.set_lang("en")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.runAndWait()

# Function to take user command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 2
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said  :  {query}\n")

        except Exception as e:
            print("Say that again, please..")
            return "None"
        return query


# Function to perform Wikipedia search
def search_wikipedia(query):
    try:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There were multiple matching results. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        speak("Sorry, I couldn't find any information on that topic.")

# Function to open websites
def open_website(url, name):
    webbrowser.open(url)
    speak(f"Opening {name}")

# Function to check internet speed
def check_internet_speed():
    speak("Checking internet speed...")
    st = speedtest.Speedtest()
    ds = st.download()
    us = st.upload()
    speak(f"Download speed is {ds} Mbps, Upload speed is {us} Mbps")

# Function to play music from PC
def play_music():
    speak("Playing music from your PC...")
    music_dir = 'E:\\Music'  # Replace with your music directory
    musics = os.listdir(music_dir)
    songno = random.randint(1, len(musics))
    os.startfile(os.path.join(music_dir, musics[songno]))

# Function to open camera
camera_thread_running = False
import threading
def open_camera():
    global camera_thread_running
    speak("Opening the camera...")

    # Start the camera thread
    camera_thread_running = True
    camera_thread = threading.Thread(target=camera_thread_function)
    camera_thread.start()

    # Wait for user input to stop the camera
    # input("Press Enter to stop the camera...")
    cm = takeCommand().lower()
    if("stop" or "stop camera" in cm):
        # Set the camera thread flag to False to stop it
        camera_thread_running = False
        camera_thread.join()
  

def camera_thread_function():
    global camera_thread_running
    cap = cv2.VideoCapture(0)

    while camera_thread_running:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5,
                           interpolation=cv2.INTER_AREA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
# Function to open task manager
def open_task_manager():
    speak("Opening Task Manager...")
    try:
        os.system("taskmgr")
    except Exception as e:
        print(e)
        speak("Sorry, I am unable to open Task Manager at the moment.")

# Function to remember a message
def remember_message():
    speak("What should I remember?")
    memory = takeCommand().lower()
    with open('memory.txt', 'w') as file:
        file.write(memory)
    speak("I have remembered that.")

# Function to recall a remembered message
def recall_message():
    try:
        with open('memory.txt', 'r') as file:
            memory = file.read()
        speak(f"You asked me to remember: {memory}")
    except FileNotFoundError:
        speak("I don't have any remembered messages.")

# Function to write a note
def write_note():
    speak("What should I write in the note?")
    note = takeCommand().lower()
    file_name = 'note.txt'
    with open(file_name, 'w') as file:
        file.write(note)
    speak("The note has been written.")

# Function to show a written note
def show_note():
    try:
        with open('note.txt', 'r') as file:
            note = file.read()
        speak("Here is the note:")
        speak(note)
    except FileNotFoundError:
        speak("There are no notes available.")

# Function to set an alarm
def set_alarm():
    speak("At what time would you like to set the alarm?")
    alarm_time = input("Enter the time in HH:MM format: ")
    current_time = datetime.datetime.now().strftime("%H:%M")
    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M")
        time.sleep(1)
    speak("Time to wake up!")
    os.system("start your_alarm.mp3")

# Function to send an email
def send_email():
    try:
        speak("Whom do you want to send the email to?")
        to = takeCommand().lower()
        to = to.replace(' ', '')
        print(to)
        speak("What is the subject of the email?")
        subject = takeCommand()
        speak("Do you want to add an attachment to this email?")
        response = takeCommand().lower()

        if "yes" in response:
            speak("Please tell me the file location to attach")
            path = input("Please provide the proper path: ")
            speak("What is the message for this email?")
            message = takeCommand()
            speak("Please wait, I am sending the email now...")
            # Send the email with attachment
            # ...

        elif "no" in response:
            speak("What is the message for this email?")
            message = takeCommand()
            speak("Please wait, I am sending the email now...")
            # Send the email without attachment
            # ...

        speak("Email has been sent.")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send the email at the moment.")

# Function to play songs on YouTube
def play_songs_on_youtube():
    speak("Which song would you like to play?")
    song = takeCommand()
    if "any song" in song or "your favorite song" in song:
        song = "See You Again"  # Replace with your favorite song
    kit.playonyt(song)
    speak(f"Playing {song}")

# Function to remove ads on YouTube
def remove_youtube_ads():
    speak("Removing ads on YouTube...")
    # Code to remove ads
    # ...

# Function to check battery percentage
def check_battery_percentage():
    speak("Checking battery percentage...")
    # Code to check battery percentage
    # ...

# Function to scroll down the screen
def scroll_down_screen():
    speak("Scrolling down the screen...")
    pyautogui.mouseDown(x=10, y=20, button='left')

# Function to minimize the window
def minimize_window():
    speak("Minimizing the window...")
    pyautogui.hotkey("win", "d")

# Function to go full screen
def full_screen():
    speak("Going full screen...")
    pyautogui.hotkey("f11")

# Function to send a WhatsApp message
def send_whatsapp_message():
    try:
        speak("Whom do you want to send the WhatsApp message to?")
        contact_name = takeCommand()
        speak("What message would you like to send?")
        message = takeCommand()
        speak("Please wait, I am sending the WhatsApp message now...")
        # Code to send WhatsApp message
        # ...
        speak("WhatsApp message has been sent.")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send the WhatsApp message at the moment.")

# Function to open Instagram profile
def open_instagram_profile(username):
    try:
        speak("Opening Instagram profile...")
        insta_profile = instaloader.Instaloader()
        insta_profile.download_profile(username, profile_pic_only=True)
        speak(f"Opening Instagram profile of {username}")
        webbrowser.open(f"https://www.instagram.com/{username}")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to open the Instagram profile at the moment.")

# Function to read a PDF file
def read_pdf_file(file_path):
    try:
        speak("Reading the PDF file...")
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            num_pages = pdf_reader.numPages
            speak(f"The PDF file contains {num_pages} pages. Which page would you like to read?")
            page_number = int(input("Page number: ")) - 1
            if page_number >= 0 and page_number < num_pages:
                page = pdf_reader.getPage(page_number)
                text = page.extractText()
                speak("Here is the text from the PDF page:")
                speak(text)
            else:
                speak("Invalid page number.")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to read the PDF file at the moment.")

# Function to search Google
def search_google(query):
    try:
        speak("Searching Google...")
        search_results = search(query, num_results=5)
        for i, result in enumerate(search_results, start=1):
            speak(f"Result {i}: {result}")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to perform the Google search at the moment.")

# Function to get weather information
def get_weather():
    try:
        speak("Please tell me the name of the city or location for which you want to know the weather.")
        location = takeCommand()
        speak("Please wait, I am fetching the weather information...")
        # Code to fetch weather information
        # ...
        speak("Here is the weather information for " + location)
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to fetch the weather information at the moment.")

# Function to get Wolfram Alpha results
def get_wolfram_alpha_results(query):
    try:
        speak("Please wait, I am fetching information from Wolfram Alpha...")
        response = wolfram_alpha_client.query(query)
        for pod in response.pods:
            if pod.title:
                speak(pod.title)
            for sub in pod.subpods:
                if sub.plaintext:
                    speak(sub.plaintext)
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to fetch information from Wolfram Alpha at the moment.")

# Function to generate text using OpenAI GPT-3
def generate_text_with_gpt3(prompt):
    try:
        speak("Generating text using GPT-3...")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100
        )
        generated_text = response.choices[0].text
        speak("Here is the generated text:")
        speak(generated_text)
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to generate text using GPT-3 at the moment.")
    except ConnectionError as e:
        print(e)
        speak("Sorry, I am currently unable to connect to the GPT-3 service.")


def taklWithBot(query,takeCommand,bot):
    speak("sure ")
    query = takeCommand().lower()
    if query:
            response = bot.get_response(query)
            speak(response)
        


def wikipedia_search(query):
    speak("searching details....")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)
    

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("opening youtube")

def open_github():
    webbrowser.open("https://www.github.com")
    speak("opening github")

def goodbye():
    speak("Goodbye, have a great day!")
    sys.exit()

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def checkBattery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    timeleft = convertTime(battery.secsleft)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    speak(
        f"sir we have {percent} percent battery and power supply is {plugged} ")
    speak(f"Without charging we work {timeleft}")
