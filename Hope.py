import pyttsx3
import re
import urllib.parse
import urllib.request
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
import socket
from selenium import webdriver
import requests,json
import sys
import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import time
from detect import facereco
import tkinter as tk
from PIL import ImageTk,Image






def speak(audio):
   eng=pyttsx3.init()
   eng.setProperty("rate", 130)
   voices = eng.getProperty('voices')
   eng.setProperty('voice', voices[1].id)
   eng.say(audio)
   eng.runAndWait()



def time():
     Time=datetime.datetime.now().strftime("%I:%M:%S")
     speak("Current Time is ")
     speak(Time)
     print(Time)
     
     

def date():
    yr=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak("Today is")
    speak(yr)
    print(yr)
    speak(month)
    print(month)
    speak(day)
    print(day)


    
def wish():
     
         speak("Hello Im Hope ! Your Virtual Assistant")
         print("Hello Im Hope ! Your Virtual Assistant")
         speak("Welcome back Ma'am")
         print("Welcome back Ma'am")

         greet=datetime.datetime.now().hour
         if greet >=6 and greet<12:
            speak("Good Morning ! Have a great day ahead Ma'am !")
            print("Good Morning ! Have a great day ahead Ma'am !")
         elif greet >=12 and greet<18:
            speak("Good Afternoon!")
            print("Good Afternoon!")
         elif greet >18 and greet<=20:
            speak("Good Evening Ma'am!")
            print("Good Evening Ma'am!")
         else:
            speak("Have a pleasent Night Ma'am!")
            print("Have a pleasent Night Ma'am!")
            speak("Im at your service please tell me how I can help you?")  
            print("Im at your service please tell me how I can help you?")  

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening.......")
         speak("Listening.......")
         r.pause_threshold=1
         r.adjust_for_ambient_noise(source, duration=2) 
         audio=r.listen(source)
        
    try:
        print("Recoganizing....")
        fire=r.recognize_google(audio, language='en-in')
        print(fire)

    except Exception as e:
        print(e)
        speak("Sorry an issue occurred ! Please try again")
        print("Sorry an issue occurred ! Please try again")

        
    return fire


def screenshot():
    
    img=pyautogui.screenshot()
    img.save('E:/virtual assistant/screenshot/Hopess.png')
    
def cpu():
    usage=str(psutil.cpu_percent())
    status=str(psutil.cpu_stats())
    speak('CPU is at'+usage)
    print('CPU is at'+usage)
    speak('CPU status is'+status)
    print('CPU status is'+status)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    print("Battery is at")
    speak(battery.percent)
    print(battery.percent)
  
    
def joke():
    speak(pyjokes.get_joke())
    print(pyjokes.get_joke())

def remember():
     speak("What should I make you remember ?")
     data=command()
     speak("You asked me to remember"+data)
     remember=open('E:/virtual assistant/.vscode/data.txt','w')
     remember.write(data)
     remember.close()
  
def inpremember():
     print("What should I make you remember ?")
     print("Enter below")
     data=input()
     print("You asked me to remember"+data)
     remember=open('E:/virtual assistant/.vscode/data.txt','w')
     remember.write(data)
     remember.close()
  


def ask():
     speak("Any other commands Maam?")
     fire=command().lower()
     if  'yes' in fire or 'yeah' in fire or 'haa' in fire:
       speak("Ok Maam  Listening")
       command()

     else:
       speak("Thank you !")
       return "None"

def question():
    try:
         speak("Ask your question, if I know the answer then I will surely answer it !")
         question=command().lower()
         app_id = "2948TT-JAEAP77RH7" 
         client = wolframalpha.Client(app_id) 
         res = client.query(question) 
         answer = next(res.results).text
         print(answer)
         speak(answer)
    except Exception as e:
        print(e)
        speak("Sorry your command was not recoganized !!")
        return "None"

def inpquestion():
    try:
         print("Ask your question, if I know the answer then I will surely answer it !")
         question=input()
         app_id = "2948TT-JAEAP77RH7" 
         client = wolframalpha.Client(app_id) 
         res = client.query(question) 
         answer = next(res.results).text
         print(answer)
         speak(answer)
    except Exception as e:
        print(e)
        speak("Sorry your command was not recoganized !!")
        print("Sorry your command was not recoganized !!")
        return "None"    



def internet_connection():
     
    try:
        urllib.request.urlopen('http://google.com')
        speak("You are connected to internet ")
        print("You are connected to internet ")
        return True
        
    except:
        speak("No Internet Connection")
        print("No Internet Connection")
        return False
       
def NewsFromBBC(): 
      
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
  
    open_bbc_page = requests.get(main_url).json() 
  
    article = open_bbc_page["articles"] 
  
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        print(i + 1, results[i]) 
  
    from win32com.client import Dispatch 
    speak = Dispatch("SAPI.Spvoice") 
    speak.Speak(results)    
    print(results)           
def screenrec():

# display screen resolution, get it from your OS settings
      SCREEN_SIZE = (1920, 1080)
# define the codec
      fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
      out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

      while True:
    # make a screenshot
        img = ImageGrab.grab()
    # img = pyautogui.screenshot(region=(0, 0, 300, 400))
    # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
    # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
        out.write(frame)
    # show the frame
        cv2.imshow("screen Recorder", frame)
        
    # if the user clicks q, it exits
        if cv2.waitKey(1) == ord("q"):
            break

# make sure everything is closed when exited
      cv2.destroyAllWindows()
      out.release()
