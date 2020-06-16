#required modules for the program
import pyttsx3
import datetime
import speech_recognition as sr 
import webbrowser
import wikipedia
import os 
import requests
# import googlesearch

#engine 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    #run and wait for the user's command
    engine.runAndWait()

#greeting programme to wish the user 
def wishMe():
    
    #whishing according to time of the day
    hour = int(datetime.datetime.now().hour) 
    if hour >= 0 and hour < 12:
        print("Mark : Good Morning!,hey there")
        speak("Good Morning!, hey there")
        
    elif hour >= 12 and hour < 18:
        print("Mark : Good Afternoon!,hey there")
        speak("Good Afternoon!,hey there")
    
    else:
        print("Mark : Good Evening!,hey there")
        speak("Good Evening!,hey there")
          
    print("Mark : I am Mark. your virtual assistant, please tell me how can i help you? ")      
    speak("I am Mark. your virtual assistant, please tell me how can i help you? ")      

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mark : am Listening...")
        speak("am Listening")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
        print("Mark : trying to Recognize")
        speak("trying to Recognize")
        query = r.recognize_google(audio,key= None , language ='en-US')
        print("user said:\n",{query})
    
    except Exception as e:
        print(e)
        print("Mark : say that again please..")
        speak("say that again please..")
        return "None"
    return query

if  __name__ == "__main__":
    wishMe()
    while True:        
        query = takeCommand().lower()
        
        #searches wikipedia for answer
        if 'wikipedia' in query:
            print('Mark : searching wikipedia...give me some time please')
            speak('searching wikipedia...give me some time please')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            print("Mark : According to wikipedia\n")
            speak("According to wikipedia")
            print("Mark : ")
            print(results)
            speak(results)
        
        #open's youtube in the webbrowser
        elif 'open youtube' in query:
            print('Mark : opening youtube , just for u boss')
            speak('opening youtube , just for u boss')
            webbrowser.open("https://www.youtube.com")
        
        #open's google in the webbrowser    
        elif 'open google' in query:
            print("Mark : opening google , !!searching something usefull !! ")
            speak("opening google , !!searching something usefull !! ")
            webbrowser.open("https://www.google.com")
        
        #open's instagram in the webbrowser
        elif 'open instagram' in query:
            print("Mark : opening instagram, double tap to like <3 !!")
            speak("opening instagram, double tap to like <3 !!")
            webbrowser.open("https://www.instagram.com")
        
        #plays songs from local DIR
        elif 'play songs' in query:
            print("Mark : ok playing, your songs, have fun !!")
            speak("ok playing, your songs, have fun !!")
            music_dir = 'C:\\Users\\jayes\\Desktop\\my stuff\\my songs'
            music = os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir,music[0]))
        
        #tells the current local time in 24hr format       
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("boss , the time is.. ",{strTime})
            speak(f"boss , the time is.. {strTime}")
        
        #opens gtav.exe from the source    
        elif 'open gta ' in query:
            print("Mark : opening GTA v , dont play for time boss !!")
            speak("opening GTA five , dont play for time boss !!")
            gta_path = 'D:\\Games\\Grand Theft Auto V'
            os.startfile(gta_path)
        
        #to greet mom
        elif 'mummy' in query:
            print("Mark : namaste mummyji")
            speak("namaste mummyji")

        #to greet dad
        elif 'papa' in query:
            print("Mark : Namaste papaji")
            speak("namaste papaji")
            
        #to greet sir 
        elif 'sir' in query:
            print("Mark : vanakam sir")
            speak("vanakam sir")
         
        elif 'joke' in query:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
            if res.status_code == requests.codes.ok:
                takeCommand(str(res.json()['jokes']))
            else:
                takeCommand("oops!I ran out of jokes")
         
        elif  'jayesh' in query:
            print("Mark : jayesh seth is a talented boy ") 
            speak("jayesh seth is a talented boy")     
        
        elif 'who are you' in query:
            print("Mark : iam a virtual assistant made by MR.jayesh seth")
            speak("iam a virtual assistant made by MR.jayesh seth")                   
                  
        #terminates/exits the programme    
        elif 'bye' in query:
            print("Mark : good bye, see you soon")
            speak("good bye, see you soon")
            exit()