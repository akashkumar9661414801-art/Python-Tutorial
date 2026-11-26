import speech_recognition as sr#convert spoken audio into text
import webbrowser
import pyttsx3 #convert text to speech
import requests
from google import genai
from google.genai import errors
import time
import os
from dotenv import load_dotenv

load_dotenv()



recognizer=sr.Recognizer()
newsapi = os.getenv("newsapi")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")



client = genai.Client(api_key=GEMINI_API_KEY)
MODELS = ["gemini-3.8-flash", "gemini-3.5-flash-lite"]
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"




def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop() 
    engine.setProperty("rate", 120) 


def ask_gemini(question):
    prompt = "Answer briefly in 1-2 sentences, in plain text with no markdown: " + question
    for model in MODELS:
        for attempt in range(3):
            try:
                response = client.models.generate_content(model=model, contents=prompt)
                return response.text
            except errors.ServerError:
                time.sleep(2 * (attempt + 1))  # busy server, wait and retry
            except errors.ClientError as e:
                print(f"{model} failed: {e}")
                break  # try next model
    return "Sorry, the AI is busy right now. Please try again."

def is_goodbye(text):
    # remove spaces so "good bye" and "goodbye" both match
    t = text.lower().replace(" ", "")
    return "ok"in t or "good bye" in t or "bye" in t or "okgoodbye" in t or "okgoodbye" in t.replace(",", "")




def  processCommand(c):
    if is_goodbye(c):
        speak("Goodbye!!")
        return False



    if "open google" in c.lower():
        webbrowser.open("http://google.com")    
    elif "open instagram" in c.lower():
        webbrowser.open("http://instagram.com")    
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    
                 
        

    elif "news" in c.lower():
        r=requests.get(url)
        # Convert response into JSON
        data = r.json()
        # Check API response
        if data["status"] == "ok":

         articles = data["articles"]
         speak("Welcome to Python news...")

        for article in articles:
            speak( article["title"])
            print("Source:", article["source"]["name"])
            print("URL:", article["url"])
            print("-" * 60)

        else:
            print("Error:", data)
        
    else:
        #let gemini ai handle the request
        speak("telling your answer")
        speak(ask_gemini(c))
        speak("yes completed")



if __name__=="__main__":
    speak("Activating alexa")
    r=sr.Recognizer()
    
    while True:
      #listen for the wake word"ALexa"
      
      
      try:
      #obtain the audio from the microphone
        with sr.Microphone() as source:
         print("Listening.. for the wake word")
         audio=r.listen(source,timeout=5,phrase_time_limit=7)
        word=r.recognize_google(audio)
        print(f"Heard {word}")

         # stop if "ok goodbye" is heard at the wake-word step
        if is_goodbye(word):
             speak("Goodbye!")
             break



        
        if "alexa" in word.lower():
            speak("Yeah tell me your problem")
           #Listen for command
            with sr.Microphone() as source:
                 print("Alexa is ON now")
                 print("give me the command")
                 audio=r.listen(source,timeout=5,phrase_time_limit=7)
                 command=r.recognize_google(audio)
                 print("Command:",command)
                 speak(f"Your command is {command}")
                 processCommand(command)
            # stop if "ok goodbye" is heard at the command step
            if is_goodbye(command):
                speak("Goodbye!")
                break



      except sr.WaitTimeoutError:
          print("No speech detected, try again")
      except sr.UnknownValueError:
          print("Could not understand audio")
      except sr.RequestError as e:
          print("Request failed:", e)
      


    

