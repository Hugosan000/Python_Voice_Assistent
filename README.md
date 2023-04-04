# Python_Voice_Assistent


This is a Python code that creates a basic voice assistant capable of performing some simple tasks. It uses the SpeechRecognition library for speech recognition, the pyttsx3 library for voice synthesis, and the datetime library to get the current time.

The voice assistant is activated when it hears the name "Python" in a voice command. Some of the tasks it can perform include responding to greetings, telling the current time, performing Google searches, and opening the operating system's Notepad or Calculator.

The code has three main functions: "speak" to synthesize voice, "listen" to capture voice commands, and "perform_task" to execute tasks based on the received commands. The main loop of the code is responsible for calling these functions repeatedly while the voice assistant is active.

The SpeechRecognition library uses a microphone to capture audio and converts it into text through various speech recognition APIs. The pyttsx3 library uses the text input to synthesize natural-sounding speech output. The datetime library is used to get the current time for the "what time is it?" task. The webbrowser library is used to open the browser and perform Google searches. The os library is used to execute system commands to open Notepad or Calculator.

The code is designed to handle voice commands in the Portuguese language with the "recognize_google" function set to the 'pt-BR' language. The program is capable of understanding and interpreting voice commands with varying degrees of accuracy based on the quality of the audio input and the complexity of the command given.
