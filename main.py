from tkinter import *
from tkinter import ttk
import time
import os
import datetime
import playsound
import random
import speech_recognition as sr
from gtts import gTTS




#variables and arrays
welcom=["hello","hi","hi eliza robot","hey"]
robotwelcom=["hey","hello","how are you","hello my name is eliza robot","hello salah"]
howareyou=["how are you","are you fine"]
howareyourobot=["fine","I am fine and you","not fine","eliza robot not fine I am sad"]
wname=["your name","name please","what is your name"]
wtime=["time","what is the time now","what is the time","time please","hour","clock","clock please","what time is it"]
wdate=["dite","dete","dyte","what is the date today","what is the date","date please","dyte please","date","today date","today dite","today dyte","dite please","what date is it"]
nameoftoday=datetime.datetime.now().strftime("%A")
year=datetime.datetime.now().year
alldate=datetime.datetime.now().strftime("%x")
todayor="today is {} in year {} and complete date is {}".format(nameoftoday,year,alldate)
namerobot="my name is eliza robot made by salah"
probleme=["sorry I do not understand","I can not answer","Are you kidding me? I don't get you","Say hello first","Say hello at least","I do not want to talk now"]
nottalk="not talk"


#listen user function for listen sound
def listen_user():
  rec=sr.Recognizer()
  with sr.Microphone() as source:
    rec.adjust_for_ambient_noise(source,duration=1)
    print("mr robot is listening")
    
    audio=rec.listen(source,phrase_time_limit=3)
  try:
    text=rec.recognize_google(audio,language='en-US')
     
    return text
  except:
    text=nottalk
    return text


#talk  function for make talk sound
def talk(text,file):
  tts=gTTS(text,lang="en")
  
  filename="%s.mp3"%file
  tts.save(filename)
  playsound.playsound(filename,True)

  os.remove(filename)




  

#contact  function for  talk with user
def contact():
  while True:
      

      result = time.localtime(1545925769)
      de=random.randint(1,30000)
      countertime=de+result.tm_year+result.tm_mday+result.tm_hour+result.tm_min+result.tm_sec


      alltime=datetime.datetime.now().strftime("%X")
      timeor="time is {}".format(alltime)

      
      choi=random.choice(robotwelcom)
      prob=random.choice(probleme)
      how=random.choice(howareyourobot)


      text_returnd=listen_user()

      if text_returnd in welcom:
        print(choi)
        talk(choi,countertime)
        
      


      elif text_returnd in wname:
        print(namerobot)
        talk(namerobot,countertime)



      elif text_returnd in howareyou:
        print(how)
        talk(how,countertime) 
        


      elif text_returnd in wtime:
        print(timeor)
        talk(timeor,countertime) 
        


      elif text_returnd in wdate:
        print(todayor)
        talk(todayor,countertime) 

      
   


      else:
        print(prob)
        talk(prob,countertime)
      

      time.sleep(2)



root = Tk()
root.title("eliza robot")
root.geometry("520x600")
root.resizable(False,False)


image =PhotoImage(file="as.gif")
Label(root, image=image).place(x=0,y=0)
ttk.Button(root,text="start Talk with me",command=lambda:contact()).grid(column=0,row=0,padx=40,pady=15,ipadx=2,ipady=2)
root.mainloop()
        
        

   
      
     


