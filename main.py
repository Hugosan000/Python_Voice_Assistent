import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pyaudio

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice assistant's name
assistant_name = "Python"

# Define a function for the voice assistant to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen for commands
def listen():
    with sr.Microphone() as source:
        print("How can I help you?")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I didn't understand. Could you please repeat?")
            command = listen()
        return command

# Define a function to perform tasks based on the command
def perform_task(command):
    if "hello" in command or "hi" in command:
        speak(f"Hello, how are you today?")
    elif "what time is it" in command:
        now = datetime.datetime.now()
        speak(f"The time is {now.strftime('%I:%M %p')}")
    elif "search" in command:
        query = command.replace("search", "")
        webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
        speak(f"Here's what I found for {query} on Google")
    elif "create a to-do list" in command:
        os.system("notepad.exe")
    elif "set a reminder" in command:
        os.system("calc.exe")

# Main loop
while True:
    command = listen().lower()
    if assistant_name in command:
        perform_task(command)
