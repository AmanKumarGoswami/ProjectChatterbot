import templates
import training as tr
import win32com
import speech_recognition as sr
from time import ctime
import time
import os
#from gtts import gTTS
import audio_find as find
from random import randrange
import webbrowser as wb
from flask import Flask, render_template, request, redirect, Response
import random, json
value = 0

app = Flask(__name__)

@app.route('/')
def output():
	return render_template("design.html")


def speak(audioString):

    print("B: " + audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)


def recordAudio():
    #Record Audio
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.energy_threshold = 280  # minimum audio energy to consider for recording

        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.15
        dynamic_energy_ratio = 0.1
        r.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
        r.operation_timeout
        from win32com.client import constants
        import win32com.client
        import training as tr
        # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

        r.phrase_threshold = 0.1   #minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        r.non_speaking_duration = 0 # seconds of non-speaking audio to keep on both sides of the recording

        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        speak("Say something!")
        speak("Can you speak")
        audio = r.listen(source, phrase_time_limit=4)
    data = ""
    try:
        print("Audio Recorded")
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language='en-IN')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        check = 1
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

@app.route('/receiverT', methods=['POST'])
def news_head4():
    jsonData = request.get_json()
    data = jsonData['id']
    print(data)
    if "text" == data:
        return 'In which language would you like to see your news! <INPUT type="sub" value="Hindi" onclick="callNewsApi(\'hindi-text\')"> or <INPUT type="sub" value="English" onclick="callNewsApi(\'english-text\')">'
    elif "video" == data:
        return 'In which language would you like to see your news! <INPUT type="sub" value="Hindi" onclick="callNewsApi(\'hindi-video\')"> or <INPUT type="sub" value="English" onclick="callNewsApi(\'english-video\')">'
    elif "hindi-text" == data:
        wb.open("https://www.bhaskar.com/national/", new=0, autoraise=True)
        return "opening news in hindi"
    elif "english-text" == data:
        wb.open("https://timesofindia.indiatimes.com/home/headlines", new=0, autoraise=True)
        return "opening news in english"

    elif "hindi-video" == data:
        wb.open("https://www.youtube.com/watch?v=smZRzehsXHA", new=0, autoraise=True)
        return "opening news in hindi"
    elif "english-video" == data:
        wb.open("https://www.youtube.com/watch?v=WmutmzNRIx8", new=0, autoraise=True)
        return "opening news in english"


@app.route('/receiver', methods=['POST'])
def search_data():
    jsonData = request.get_json()
    data = jsonData['id']
    if data:
        if "hi" in data or "hello" in data or "hey" in data:
            #speak("hi what can i do for you")
            # return statement is used for JSON here
            return "hi what can i do for you"

        elif 'time now' in data or 'time please' in data or 'tell me the time' in data:
            return"now time is" + ctime()
            #speak("now time is" + ctime())

        elif "your name" in data:
            return "I am a robot"
            #speak("I am a robot")

        elif "dead" in data:
            return "no, i am just a machine"
            #speak("no, i am just a machine")

        elif "bye" in data:

            return "bye! have a nice day! See you soon"
            exit()
            #speak("bye! have a nice day! See you soon")

        elif "weather report" in data:
            #speak("Opening weather news")
            wb.open("https://www.google.com/search?ei=O5OjXKmKKMb39QPUkL-wCg&q=weather+today+in+jabalpur&oq=weather+today+in+jab&gs_l=psy-ab.1.0.0i70i256j0l3j0i22i30l3j0i22i10i30j0i22i30l2.27940.40180..42499...0.0..0.423.3545.0j4j10j0j1......0....1..gws-wiz.......0i71j35i39i285i70i256j35i39j0i131i67j0i67j0i131j0i20i263.HQpagm5Pgg8",new=0, autoraise=True)
            return "opening weather news"
            #speak("i am ready to take new command")

        elif 'open Reddit python' in data:
            #speak("open Reddit python")
            wb.open("http://www.reddit.com/r/python", new=0, autoraise=True)
            return "open Reddit python"
            #speak("i am ready to take new command")

        elif "start training" in data or "train yourself" in data:
            tr.training_start()

        elif "news" in data:
            return 'In which format do you like to see news! <INPUT type="sub" value="Text" onclick="callNewsApi(\'text\')"> or <INPUT type="sub" value="Video" onclick="callNewsApi(\'video\')">'


        elif 'what\'s up' in data:
            return 'Chilling bro'
            #speak('C3hilling bro')

        else:
            find.find_text(data)
#initialization
time.sleep(2)
#speak("Hi sir, How can i help you.")
#while 1:
    #data = input()
    #data = recordAudio()
    #search_data(data)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True
    FLASK_DEBUG = 1
    app.run("localhost", "5010")

