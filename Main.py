
import pyautogui
import pyttsx3
import datetime
import speech_recognition as sr
import subprocess as sp
import os
import wikipedia
import webbrowser
import pywhatkit
import re
import pyjokes
import time
from PIL import Image
import branch
import keyboard
import pygetwindow as gw
import requests

obj =()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("good evening")
    
    else:
        speak("Good Evening sir")

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def close_camera():
    speak("Closing the camera")
    # Replace 'CameraApp.exe' with the actual process name of your camera application
    #os.system("taskkill /f /im CameraApp.exe")
    os.system("taskkill /f /im windowscamera.exe")

def pause_music():
    speak("Pausing music")
    keyboard.press_and_release('space')

def stop_music():
    speak("Stopping music")
    # Replace 'ctrl + q' with the appropriate keyboard shortcut to stop or close your media player
    keyboard.press_and_release('alt + F4')

def google_search(query):
    speak(f"Searching Google for {query}")
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def go_back_vs_code():
    speak("Going back to tab")
    try:
        # Simulate the keyboard shortcut for going back in Visual Studio Code (Ctrl + -)
        pyautogui.hotkey('alt', 'tab')
    except Exception as e:
        print(f"Error going back to Visual Studio Code: {e}")
        speak("Sorry, I encountered an error while trying to go back to Visual Studio Code.")

def close_google():
    speak("Closing Google")
    try:
        # Close the default web browser
        os.system("taskkill /f /im chrome.exe")  # Adjust this command based on your default browser
    except Exception as e:
        print(f"Error closing Google: {e}")
        speak("Sorry, I encountered an error while trying to close Google.")

def close_youtube():
    speak("Closing YouTube")
    try:
        # Simulate the keyboard shortcut for closing a tab (Ctrl + W)
        pyautogui.hotkey('ctrl', 'w')
    except Exception as e:
        print(f"Error closing YouTube: {e}")
        speak("Sorry, I encountered an error while trying to close YouTube.")

def close_current_tab():
    speak("Closing the current tab")
    try:
        # Simulate the keyboard shortcut for closing the current tab (Ctrl + W)
        pyautogui.hotkey('ctrl', 'w')
    except Exception as e:
        print(f"Error closing the current tab: {e}")
        speak("Sorry, I encountered an error while trying to close the current tab.")

notes = []

def take_note(note_text):
    notes.append(note_text)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant information from the API response
            main_info = data.get('main')
            if main_info:
                temperature = main_info.get('temp')
                weather_description = data['weather'][0]['description']

                weather_result = f"In {city}, the temperature is {temperature} degrees Celsius, and the weather is {weather_description}."
                return weather_result
            else:
                error_message = f"Error fetching weather data. Unexpected response format: {data}"
                print(error_message)
                return "Sorry, I couldn't retrieve the weather information."

        else:
            error_message = f"Error fetching weather data. Status code: {response.status_code}, Response: {data}"
            print(error_message)
            return "Sorry, I couldn't retrieve the weather information."

    except Exception as e:
        error_message = f"Error fetching weather data: {e}"
        print(error_message)
        return "Sorry, I couldn't retrieve the weather information."

# ... (other code)

def capture_screenshot():
    # ... (code to capture screenshot)
        name = "example_screenshot"  # Set an example value for 'name'
        return name

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pouse_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

        if 'exit' in query or 'stop' in query:
            speak('Alright sir, going offline. It was nice working with you')
            exit()

    except Exception as e:
      #  print(e)
        speak("Sorry, say that again please")
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    
   wishme()
   while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'hello jarvis' in query:
        speak("hello sir, how are you ?")

    elif 'fine' in query:
        speak("Good to hear that sir, what to do next?")

    elif 'search' in query:
    # Extract the search query from the user's command
        search_query = query.replace(" open google", "").replace("search", "").strip()
        google_search(search_query)
    
    elif 'close google' in query or 'exit google' in query:
        close_google()

    elif 'play music' in query:
        speak("okay sir, playing music")
        music_dir = 'E:\\Sounds'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        
    elif 'pause music' in query or 'stop music' in query:
        pause_music()
    
    elif 'stop music' in query or 'close music' in query:
        stop_music()
 
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'date' in query:
        strDate = datetime.datetime.now().strftime("%D:%M:%Y")
        speak(f"Sir, date is {strDate}")

    elif 'open camera' in query:
        speak("okay sir, openinig camera")
        open_camera()

    elif 'close camera' in query or 'exit camera' in query:
        close_camera()
    
    elif 'hand gestures' in query:
        speak("okay sir, starting hand gestures")
        branch.hand_track()

    elif 'open vs code' in query:
        codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening VS Code")
        os.startfile(codePath)
    
    elif 'close vs code' in query or 'exit vs code' in query:
        speak("Closing VS Code")
        os.system("taskkill /f /im Code.exe")
    
    elif 'back to tab' in query:
        go_back_vs_code()

    elif 'who are you' in query:
        speak("i am jarvis , your ai assistant")
    
    elif 'are you ' in query:
        speak("yes sir, I am here")

    elif 'chrome' in query:
        codePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        speak("Opening chrome")
        os.startfile(codePath)

    elif 'spotify' in query:
        speak("Opening spotify")
        webbrowser.open("spotify.com")

    elif 'news' in query:
        speak("today news")
        webbrowser.open("timesofindia.com")
    
    elif 'whatsapp' in query:
        speak("Opening Whatsapp")
        webbrowser.open("web.whatsapp.com")
    
    elif 'close tab' in query or 'close current tab' in query:
        close_current_tab()

    elif 'youtube' in query:
                video = query.split(' ')[1]
                speak(f"Okay sir, playing {video} on youtube")
                pywhatkit.playonyt(video)

    elif 'youtube close' in query or 'exit youtube' in query:
        close_youtube()

    elif re.search('weather', query):
        city = query.split(' ')[-1]
        api_key = 'your_openweathermap_api_key'
        weather_result = get_weather(api_key, city)
        print(weather_result)
        speak(weather_result)

    elif 'make a note' in query or 'write this down' in query or 'remember this' in query:
        speak("What would you like me to write down?")
        note_text = takeCommand()
        take_note(note_text)
        speak("I've made a note of that")

    if "joke" in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)
    
    elif "take screenshot" in query or "take a screenshot" in query or "capture the screen" in query:
                speak("By what name do you want to save the screenshot?")
                name =takeCommand()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")

    elif "show me the screenshot" in query:
        name = capture_screenshot()  # Call the function that captures the screenshot and sets 'name'
        if name is not None:
            img_path = f'D:\\Python\\Projects\\{name}.png'  # Assuming the image has a .png extension
        try:
            img = Image.open(img_path)
            img.show()
            speak("Here it is, sir")
            time.sleep(2)
        except FileNotFoundError:
            speak("I couldn't find the screenshot.")
        else:
            speak("No screenshot has been taken yet.")
    
    #elif "show me the screenshot" in query:
        #if name is not None:
            #img_path = 'D:\\Python\\Projects\\' + name + '.png'  # Assuming the image has a .png extension
        #try:
            #img = Image.open(img_path)
            #img.show()
            #speak("Here it is, sir")
            #time.sleep(2)
        #except FileNotFoundError:
            #speak("I couldn't find the screenshot.")
    #else:
        #speak("No screenshot has been taken yet.")








    
   



    

