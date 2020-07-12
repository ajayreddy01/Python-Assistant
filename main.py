import requirements
from requirements import *

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('33UPA7-YGAUU4EYQA')

voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[2].id)
engine.setProperty('voices',voices[len(voices)-1])
#engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 135)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetme()

speak('Hello , I am digital assistant! ')
#speak('How May I Help You?')
def command():
#    r = sr.Recognizer()
  #  with sr.Microphone() as source:
    #    speak("Listening...")
    #    r.pause_threshold =  1
      #  audio = r.listen(source)
   # try:
        #query = r.recognize_google(audio, language='en-in')
        #speak('User: ' + query + '\n')
        
    #except sr.UnknownValueError:
     #speak('Sorry ! I didn\'t get that! Try typing the command!')
    query = str(input())
    return query
if __name__ == '__main__':
    while True:
        query = command();
        query = query.lower()
        if 'date' in query:
            today =datetime.datetime.now().today
            speak(today)
            #today = int(today)
            month = datetime.datetime.now().month
            speak(month)
            year= datetime.datetime.now().year
            speak(year)
            print(today,":",month,":",year)
        elif 'time' in query:
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            sec = int(datetime.datetime.now().second)
            speak(hour)
            speak(minute)
            speak(sec)
            print(hour,":",minute,":",sec)
        elif 'instagram'  or 'ig'in query:
            speak('Opening Instagram!')
            from instagram import insta
            insta()
        elif 'whatsapp' in query:
            speak('Opening whatsapp!')
            from whatsapp import whatsapp
            whatsapp()
        elif 'facebook' or 'fb' in query:
            speak('Opening Facebook!')
            from facebook import fb
            fb()
        elif  'send eamil' or 'mail' or 'email' in query:
            speak('Intializing Process To Send Email!')
            from email_bot import email_bot
            email_bot()
        elif  'voice recorder'  or 'record voice'  or 'record sound' or 'sound recorder' in query:
            speak('Starting Sound recorder')
            from Sound_Recorder import Sound_Recorder
            Sound_Recorder()
        elif 'paly music'  or 'play some music' or 'music player' in query:
            speak('Starting Music player')
            from Music_Player import Music_Player
            Music_Player()
        elif  'movie rating'  'get movie rating' or 'movie details' in query:
            speak('Getting Details Using IMBD')
            from Movie_Rating import Movie_Rating
            Movie_Rating()
        elif 'pencil art' in query:
            speak('Intializing Process For Pencil Art')
            from pencil_art import pencil_art
            pencil_art()
        elif 'vector art' in query:
            speak('Intializing Process For Vector Art')
            from vector_art import vector_art
            vector_art()
        elif  'screen recorder' in query:
            speak('Starting Screen recorder')
            from Screen_Recorder import Screen_Recorder
            Screen_Recorder()
        elif  'twitter' in query:
            speak('Opening twitter')
            from twitter import twitter
            twitter()
        elif 'close' or 'bye' or 'exit' in query:
            sys.exit()
        else:
            query = query
            speak("searching")
            try:
                res = client.query(query)
                results = next(res.results).text
                speak(results)
                print(results)
            except:
                results = wikipedia.summary(query)
                speak('Getting Details From Wikipedia')
                speak(results)
                print(results)
        speak("NEXT COMMAND ")
