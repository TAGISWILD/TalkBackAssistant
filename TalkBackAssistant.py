import speech_recognition as sr
import os
from gtts import gTTS
import random
import playsound
import time
import wikipedia
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def speaker(ToSpeak):
    tts = gTTS(text=ToSpeak, lang = 'en', slow=False)
    Filename = random.randint(1,1000000)
    audio_file = 'audio-' +str(Filename) + '.mp3'
    tts.save(audio_file)
    playsound.playsound("over.mp3")
    playsound.playsound(audio_file)
    print(ToSpeak)
    os.remove(audio_file)

def listener():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
                speaker("Sorry, I didn't get that.")
        except sr.RequestError:
                speaker("There was a request error.")
                
def responder(cmmnd):
    if 'what is your name' in cmmnd:
        speaker ('My Name Is rani')
    elif 'who made you' in cmmnd:
        speaker("I am made by sir. Atharva Chauhan")
    elif 'exit' in cmmnd:
        exit()
    else:
        speaker ('I am Sorry,, But I am Not Trained for it')

while(1):
    responder(listener())
    
