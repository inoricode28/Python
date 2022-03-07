import speech_recognition as sr
import pyttsx3, pywhatkit

name = "computadora"
listener = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
for i in voices:
	print(i)