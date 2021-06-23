import pyttsx3
import pandas as pd
from nltk import *
from nltk import Tree
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
import re
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser
import os
import pyautogui
import psutil
import pyjokes
import wolframalpha
import urllib.request
import urllib.parse
import cv2
import sys
import pytesseract
import random
from selenium import webdriver
import requests,json
from Hope import command,speak,ask,time,date,question,wish,remember,screenshot,cpu,joke,question,screenrec
from Hope import internet_connection,NewsFromBBC
from language import training
from detect import facereco
from win10toast import ToastNotifier
import numpy as np
from PIL import ImageGrab
import pyshorteners
from PIL import Image
import twilio
from twilio.rest import Client
from detect import facereco
import tkinter as tk
from PIL import ImageTk,Image
from Hope import *
from Main import *
from detect import *
from language import *
from database import assist_record
from database import owner_records






def inpcommand(fire):
    try:

            how=["Im fine","Im good","Im feeling nice"]
            name="HOPE"
            gender="Female"
           
            if "owner records" in fire or "owner" in fire or "owners" in fire :
                speak(owner_records())
                print(owner_records())

            if "about yourself" in fire or "yourself" in fire :
               speak(assist_record())
               print(assist_record())

            if "your name" in fire:                     #name
                speak(name)
                print(name)
            if "your gender" in fire:                  #gender
                speak(gender)
                print(gender)
            if "hindi"in fire:                         #hindi
                speak("hindi nahi sikhaya gaya hai mujhe")
                print("hindi nahi sikhaya gaya hai mujhe")
            if "your surname" in fire:                 #surname
                speak("Robo")
                print("Robo")
            if "your favourite color" in fire:        #fav color
                speak("black")
                print("black")
            if "how are you" in fire:                 #how's you?
                speak(random.choice(how))
                print(random.choice(how))

            if "hello" in fire or "hi" in fire or "hello Hope" in fire or "hi hope" in fire:
                speak("Hello,Im"+name+"How can I help you ?")
                print("Hello,Im"+name+"How can I help you ?")
                fire=command().lower()

            if 'time' in fire:                            #time
                time()
                ask()
            

            elif 'date' in fire:                          #date
                date()


            elif 'offline' in fire:                      #offline
                speak("Going Offline")
                exit()

            elif 'wikipedia' in fire:                    #wikipedia
                speak("Searching....")
                fire=fire.replace("Wikipedia","")
                result=wikipedia.summary(fire,sentences=2)
                print(result)
                speak(result)

            elif 'send email' in fire or 'mail' in fire:   
                    TO=input('Reciever mail ID:')               #email
                    subject = input('Enter subject here :')
                    message =input('Enter Body of mail:')
                    content = 'Subject: {}\n\n{}'.format(subject, message)

                    #init gmail SMTP
                    mail = smtplib.SMTP('smtp.gmail.com', 587)

                    #identify to server
                    mail.ehlo()

                    #encrypt session
                    mail.starttls()

                    #login
                    mail.login('shirinmenon05@gmail.com', 'shirin@#567')

                #send message
                    mail.sendmail('shirinmenon05@gmail.com', TO, content)

                #end mail connection
                    mail.close()

                    speak('Email sent.')
                    print('Email Sent')

            elif 'open google' in fire:                #google
                webbrowser.open("google.com")
    
            elif 'open youtube' in fire:               #youtube
                webbrowser.open("youtube.com")

            elif 'youtube' in fire:                   #play youtube
                speak('Ok!')
                reg_ex = re.search('youtube (.+)', fire)
                if reg_ex:
                    domain = fire.split("youtube",1)[1] 
                    query_string = urllib.parse.urlencode({"search_query" : domain})
                    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string) 
                    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode()) # finds all links in search result
                    webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))

            elif 'speech to text' in fire:                 #speech to text
                speak("Ok !")
                audio=command()
                print(audio)     

            elif 'search' in fire:                            #search 
                
                indx = fire.lower().split().index('search') 
                query = fire.split(' ')[-1]
                webbrowser.open ("https://www.google.com/"+ query)


            elif 'logout' in fire:                             #logout
                os.system("Shutdown -l")

            elif 'shutdown' in fire:                          #shutdown
                os.system("Shutdown /s /t 1")

            elif 'restart' in fire:                            #restart
                os.system("Shutdown /r /t 1")

            elif 'spotify'  in fire:                            #spotify
                webbrowser.open("spotify.com")

            elif 'facebook' in fire:                            #facebook
                webbrowser.open("https://www.facebook.com")
                speak("opening facebook")      

            elif 'open instagram' in fire:                      #instagram
                webbrowser.open("https://www.instagram.com")
                speak("opening instagram")    

            elif 'open gmail' in fire:                            #gmail
                webbrowser.open("https://mail.google.com")
                speak("opening google mail") 

            elif 'music' in fire or 'songs' in fire:  
                speak("Shuffling and playing music")  
                print("Shuffling and playing music")            #music
                songsdir='E:/music'
                songs= os.listdir(songsdir)
                os.startfile(os.path.join(songsdir,songs[0]))

            elif 'remember' in fire or 'notes' in fire:                              #inp-remember
                inpremember()

            elif 'Remind me' in fire or 'know something' in fire or 'know anything' in fire or 'remind me' in fire:  #remind
                remember=open('E:/virtual assistant/.vscode/data.txt','r')
                speak("You told me remember"+remember.read())
                print("You told me remember"+remember)

            elif 'screenshot'  in fire:                                                    #screenshot
                screenshot()
                speak("Screenshot Taken")
                print("screenshot taken")

            elif 'CPU'in fire or 'Battery' in fire or 'system details' in fire:                 #cpu
                cpu()

            elif 'joke' in fire  or'jokes' in fire:                                            #jokes
                joke()

            elif 'question' in fire:                                                            #gk
                inpquestion()

            elif 'calculate' in fire:                                                         #calculate
                app_id = "2948TT-JAEAP77RH7" 
                client = wolframalpha.Client(app_id) 
                indx = fire.lower().split().index('calculate')  
                fire = fire.split()[indx + 1:]  
                res = client.query(' '.join(fire))  
                answer = next(res.results).text 
                print("The answer is " + answer)  
                speak("The answer is " + answer)  

                
            elif 'open chrome' in fire:                                                           #chrome
                speak("Google Chrome") 
                os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')

            elif 'open edge' in fire:
                speak("Opening Microsoft Edge")
                os.startfile('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')

                
            elif "word" in fire:                                                                  #Ms word
                speak("Opening Microsoft Word") 
                os.startfile('C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE') 

            elif 'internet connection' in fire:                                                 # net connection
                internet_connection()

            elif 'weather' in fire:                                                                 #weathe
               
                
                api_key = "788aa8ff108fc405b5b78833b4b4c905"
                weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                location=fire.split(' ')[-1]
               
                
                url = weather_url + "appid=" + api_key + "&q=" + location
                js = requests.get(url).json() 
                if js["cod"] != "404": 
                    weather = js["main"] 
                    temp = weather["temp"] 
                    hum = weather["humidity"] 
                    desc = js["weather"][0]["description"]
                    resp_string = " The temperature in Kelvin is " + str(temp) + " The humidity is " + str(hum) + " and The weather description is "+ str(desc)
                    speak(resp_string)
                    print(resp_string)
                else: 
                    speak("City Not Found") 




            elif "map" in fire or "direction"  in fire or "location" in fire:        #map    
                tokens=word_tokenize(fire)
                stop_words=set(stopwords.words('english'))
                clean_tokens= [w for w in tokens if not w in stop_words] 
                tagged = nltk.pos_tag(clean_tokens)
                er= nltk.ne_chunk(tagged)
                print(er)
                named_entity=[]
                for tagged_tree in er:
                    print(tagged_tree)
                    if hasattr(tagged_tree,'label'):
                        entity_name=''.join(c[0] for c in tagged_tree.leaves())
                        entity_type=tagged_tree.label()
                        named_entity.append((entity_name, entity_type))
                        location_url=entity_name
               # location_url=str(Tree.label=='GPE')
                print(location_url)
                speak("Hold on, I will show you where " +location_url+ " is.")
                print("Hold on, I will show you where " +location_url+ " is.")
                webbrowser.open ("https://www.google.com/maps/place/"+ location_url)
            
            elif "who made you" in fire or "who is your owner" in fire or "who created you" in fire or" who made you hope" in fire or " who created you hope" in fire or "who is your owner hope" in fire:
                speak("I was created by Shirin Menon and Raveena Yadav..Thanks to them!")
            elif 'news' in fire:                                         #news
                NewsFromBBC() 
            elif 'training' in fire:                                     #training dataset for face recognition
                training()
            elif 'covid' in fire or 'corona' in fire:         #covid tracker
                speak("Sure ! Please Check Your Notification  ")
                r=requests.get('https://coronavirus-19-api.herokuapp.com/all')  
                data=r.json()
                text=f'confirmed cases :{data["cases"]} \nDeaths :{data["deaths"]} \nRecovered : {data["recovered"]}'
                toast=ToastNotifier()
                toast.show_toast("Covid-19 Updates",text)
            elif 'capture image' in fire or 'click picture' in fire or 'take picture' in fire:    #click image
                imgcapture=cv2.VideoCapture(0)
                ans=True
                while(ans):
                    ret,frame=imgcapture.read()
                    cv2.imwrite('Hope_captured.jpg',frame)
                    ans=False
                    speak("Image Captured")
                imgcapture.release()
            elif 'record screen' in fire or 'screen record' in fire:                #screen recorder
                screenrec()

            elif 'url shortener' in fire or 'shorten url' in fire:          #url shortner
                speak("Please enter the URL below")
                url=input("Enter URL : ")
                print("URL after shortening : ",pyshorteners.Shortener().tinyurl.short(url))
                speak("Here is your URL ")
            elif 'image to text' in fire:                        #image to text
                speak("Converting ")
                pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                path=input("Enter image path")
                img=Image.open(path)
                text=pytesseract.image_to_string(img)
                print(text)
                speak(text)
            elif 'record video' in fire:             #video recording
                speak('Recording Started')
                filename = 'video.avi'
                frames_per_second = 24.0
                res = '720p'

    # Set resolution for the video capture
    # Function adapted from https://kirr.co/0l6qmh
                def change_res(cap, width, height):
                    cap.set(3, width)
                    cap.set(4, height)

    # Standard Video Dimensions Sizes
                STD_DIMENSIONS =  {
                    "480p": (640, 480),
                    "720p": (1280, 720),
                    "1080p": (1920, 1080),
                    "4k": (3840, 2160),
                                    }


    # grab resolution dimensions and set video capture to it.
                def get_dims(cap, res='1080p'):
                    width, height = STD_DIMENSIONS["480p"]
                    if res in STD_DIMENSIONS:
                        width,height = STD_DIMENSIONS[res]
        ## change the current caputre device
        ## to the resulting resolution
                    change_res(cap, width, height)
                    return width, height

    # Video Encoding, might require additional installs
    # Types of Codes: http://www.fourcc.org/codecs.php
                VIDEO_TYPE = {
                    'avi': cv2.VideoWriter_fourcc(*'XVID'),
        #'mp4': cv2.VideoWriter_fourcc(*'H264'),
                    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
                                }

                def get_video_type(filename):
                    filename, ext = os.path.splitext(filename)
                    if ext in VIDEO_TYPE:
                        return  VIDEO_TYPE[ext]
                    return VIDEO_TYPE['avi']



                cap = cv2.VideoCapture(0)
                out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

                while True:
                    ret, frame = cap.read()
                    out.write(frame)
                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                            break


                cap.release()
                out.release()
                cv2.destroyAllWindows()
 
            elif 'send message' in fire:                                       #send message
                    account_sid = 'AC525f45b101a6a8e6e065e9ec598d8a64'
                    auth_token = '56bad9cb088fff79d025040d78a91582'
                    client = Client(account_sid, auth_token) 
                    speak("Input your message and the receiver number below")
                    message = client.messages.create( 
                                        body = input("Enter Your Message :"), 
                                        from_='+14024152665', 
                                        to =input('Receiver No : ')
                                    ) 
    
                    print("Your Messade ID is : "+message.sid) 
            elif 'detect' in fire:
                facereco()

    except Exception as e:
        return inpcommand(fire)

        
    
    
    
