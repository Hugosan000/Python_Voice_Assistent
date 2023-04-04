import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pyaudio

# Inicializa os motores de reconhecimento de fala e text-to-speech
r = sr.Recognizer()
engine = pyttsx3.init()

# Define o nome do assistente de voz
assistant_name = "Python"

# Define uma função para o assistente de voz falar
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Define uma função para ouvir os comandos
def ouvir():
    with sr.Microphone() as source:
        print("Em que posso ajudar?")
        audio = r.listen(source)
        try:
            comando = r.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")
        except sr.UnknownValueError:
            print("Desculpe, não entendi. Poderia repetir, por favor?")
            comando = ouvir()
        return comando

# Define uma função para realizar tarefas com base no comando
def realizar_tarefa(comando):
    if "olá" in comando or "oi" in comando:
        falar(f"Olá, como você está hoje?")
    elif "que horas são" in comando:
        agora = datetime.datetime.now()
        falar(f"A hora atual é {agora.strftime('%H:%M')}")
    elif "pesquisar" in comando:
        consulta = comando.replace("pesquisar", "")
        webbrowser.open_new_tab(f"https://www.google.com/search?q={consulta}")
        falar(f"Aqui está o que eu encontrei para {consulta} no Google")
    elif "criar uma lista de tarefas" in comando:
        os.system("notepad.exe")
    elif "definir um lembrete" in comando:
        os.system("calc.exe")

# Loop principal
while True:
    comando = ouvir().lower()
    if assistant_name in comando:
        realizar_tarefa(comando)
