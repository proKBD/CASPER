import pyttsx3 #pip install pyttsx3 == text data into speech using python 
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import smtplib
from email.message import EmailMessage
from secret import senderemail, epwd, to
import pyautogui #pip install pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import flask
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string 
import random
import psutil #pip install psutil
from nltk.tokenize import word_tokenize #pip install nltk
#learn from NLTK documentation
#used NLTK python 
 


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    if voice ==1:
        engine.setProperty('voice', voices[0].id)
        speak("hello this is CASPER")
    
    if voice ==2:
        engine.setProperty('voice', voices[1].id)
        speak("hello this is MARIAH")
    
    
def time():
    Time =datetime.datetime.now().strftime("%I:%M:%S") # I=hour, M=minites, S=seconds
    speak("the current time is:")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night!")
    
def wishme():
    speak("Welcome back sir!")
    # time()
    # date()
    # greeting()
    # speak("Aye Captain, CASPER at your service , please tell me how can i help you")
# while True:
#     voice=int(input("Press 1 for male voice\nPress 2 for female voice\n"))
#       # speak(audio)
#     getvoices(voice)
# time()
# date()
# wishme()

''' Section 7 , TakeCommandCMDfunction from the user'''
def takeCommandCMD():
    query = input("please tell me how can i help you?\n")
    return query

#from sec-7,part2 open
def takeCommandMIC():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again Please...")
        return "None"
    return query 


'''from Section 9 , Send Email Function'''
def sendEmail(receiver, subject, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail, epwd)
    email=EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject 
    email.set_content(content)
    server.send_message(email)
    server.close()
    
def sendwhatsmsg(phone_no, message):
    Message = message 
    wb.open('https://web.whatsapp.com/send?phone='+ phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')
    
def searchgoogle():
    speak('what should i search for?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+ search)
   
def news():
    newsapi = NewsApiClient(api_key='409f42d2ab274f1d8ed645f4ca77b03c')
    speak('Which topic you wanna search for?')
    topic = takeCommandMIC() #you can change the topic of the news from here
    data = newsapi.get_top_headlines(q=topic, 
                                     language= 'en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("that's it for now i'll update you in sime time")
        
def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)
    
def screenshot():
    name_img = tt.time()
    name_img = f'D:\\CASPER-AI project\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)
    
def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    passlen = 9
    s=[]#blank list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)
    
def flip():
    speak("okay sir, flipping a coin")
    coin = ['heads' , 'tails']
    toss =[]
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("i flipped the coin and you got"+toss)
    
def roll():
    speak("okay sir, rolling a die for you")
    die = ['1','2','3','4','5','6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak(" i rolled a die and you got"+roll)
          

if __name__ == "__main__": # syntax to write a main function in python 
    getvoices(1)
    wishme() # calling the wishme function
    wakeword = 'casper'
    while True:
        query = takeCommandMIC().lower() # this will convert the input from this function into lower case 
               #takeCommandCMD -> when we take command from terminal 
        query = word_tokenize(query)
        print(query)
        
        if wakeword in query:
            if 'time' in query:
                time()
                
            elif 'date' in query:
                date()
                
            elif 'email' in query:
                email_list={
                    'test mail': 'casper22ai@gmail.com'
                }
                try:
                    speak('To whom you want to send the mail')
                    name = takeCommandMIC()
                    receiver = email_list[name]
                    speak("What is the subject of the mail")
                    subject=takeCommandMIC()
                    speak('what should i say?')
                    content = takeCommandMIC()
                    sendEmail(receiver , subject , content)
                    speak("email has been sent")
                except Exception as e:
                    print(e)
                    speak("unable to send the email")
                    
            elif 'message' in query:
                user_name = {
                    'Omkar': '+91 89579 64906'
                }
                try:
                    speak('To whom you want to send the Whats app message?')
                    name = takeCommandMIC()
                    phone_no = user_name[name]
                    speak("What should be the message")
                    message=takeCommandMIC()
                    sendwhatsmsg(phone_no,message)
                    speak("message has been sent")
                except Exception as e:
                    print(e)
                    speak("unable to send the message")
                    
            elif 'wikipedia' in query:
                speak('searching on wikipedia...')
                query = query.replace('wikipedia', '')
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak(result)
                
            elif 'search' in query:
                searchgoogle()
                
            elif 'youtube' in query:
                speak('What should I search for in Youtube?')
                topic = takeCommandMIC()
                pywhatkit.playonyt(topic)
                
            elif 'weather' in query:
                city = 'srinagar' #you can edit the city name as per yourrequirement
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=82e63eebeec824b5190ee711c909ae22'

                res = requests.get(url)
                data = res.json()
                
                weather = data['weather'] [0] ['main']
                temp = data['main']['temp']
                desp = data['weather'] [0] ['description']
                temp = round((temp-32)*5/9) #convert farenhite to celcius
                print(weather)
                print(temp)
                print(desp)
                speak(f'weather in {city} city is like')
                speak('temperature : {} degree celcius'.format(temp))
                speak('weather is {}'.format(desp))
                
            elif 'news' in query:
                news()
                
            elif 'read' in query:
                text2speech()
            ########    
            elif 'open code' in query: #like this you can add more apps that you want to add
                codepath = 'C:\\Users\\kamya\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
                os.startfile(codepath)
            
            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('Open','')))
                #open my documents
            
            
            
            elif 'open zoom' in query: #like this you can add more apps that you want to add
                codepath = 'C:\\Users\\kamya\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
                os.startfile(codepath) 
                
            elif 'joke' in query:
                speak(pyjokes.get_joke())
                
            elif 'screenshot' in query:
                screenshot()
                
            elif 'system' in query:
                cpu()
                
            elif 'remember' in query:
                speak("What should I remember?")
                data = takeCommandMIC()
                speak("you said me to remember that"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
                
            elif 'do you know anything' in query:
                remember = open('data.txt','r')
                speak("you told me to remember that "+remember.read())
                
            elif 'password' in query:
                passwordgen()
                
            elif 'flip' in query:
                flip() #flipping a coin
                
            elif 'roll' in query:
                roll() #rolling a die 
                    
            elif 'offline' in query:
                speak('Have a good day sir!!')
                quit()
            
            elif 'quit' in query:
                speak('Have a good day sir!!')
                quit()
        
#takecommandMIC == "hey casper what is the date today" tokenize = ['hey'  , 'casper' , 'what' , 'is' , 'the' , 'date' , 'today' ]