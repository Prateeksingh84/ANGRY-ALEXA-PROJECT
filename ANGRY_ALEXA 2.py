import speech_recognition as sr
import pyttsx3



listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
     engine.say(text)
     engine.runAndWait()

def alexa_command():     
    try:

  
         with sr.Microphone() as source:
          print("listening...")
          voice=listener.listen(source)
          command=listener.recognize_google(voice)
          command=command.lower()
          if "alexa" in command:
            
            print(command)
    except:
       pass
    return command

def run_alexa():
   command=alexa_command()
   print(command)
   if "play" in command:
      song=command.replace("play","")
      talk("Playing")
      print("Playing")





run_alexa()
         


  
                 
