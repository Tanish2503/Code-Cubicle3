import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import time
import openai
from openai.error import RateLimitError, OpenAIError
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init(driverName='nsss')
newsapi = "a363519319fd41cebd6d0d2dc7923508"

openai.api_key = "sk-proj-OsRZ8cOOn4mpHpASuyJDT3BlbkFJxOYaDIAmotYQTZrLijZH"

def speak(text):
    engine.say(text)
    engine.runAndWait()  # Ensure the speech command is completed

def ai_process(command):
    def create_completion():
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks performed by Alexa and Google Cloud."},
                    {"role": "user", "content": command}
                ],
                max_tokens=100
            )
            return completion.choices[0].message['content']
        except RateLimitError as e:
            print(f"Rate limit exceeded: {e}")
            time.sleep(60)  # Wait for 60 seconds before retrying
            return create_completion()
        except OpenAIError as e:
            print(f"An error occurred: {e}")
            return "An error occurred while processing your request."

    return create_completion()

def process_command(c):
    print(f"Command: {c}")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open stackoverflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open wikipedia" in c.lower():
        webbrowser.open("https://wikipedia.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        try:
            song = " ".join(c.lower().split(" ")[1:])
            print(f"Extracted song name: {song}")
            link = musicLibrary.music[song]
            print(f"Playing link: {link}")
            webbrowser.open(link)
        except KeyError:
            print(f"Song not found: {song}")
            speak(f"Sorry, I couldn't find the song {song}")
        except Exception as e:
            print(f"An error occurred: {e}")
            speak(f"An error occurred: {e}")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        data = r.json()
        
        speak("Here are the top headlines from India")

        articles = data.get("articles", [])
        
        for article in articles:
            speak(article["title"])
            engine.runAndWait()  # Ensure each headline is spoken before moving to the next one
    elif "weather" in c.lower():
        city = " ".join(c.lower().split(" ")[1:])  # Extract the city name from the command
        get_weather(city)

    else:
        # Let OpenAI handle the request
        output = ai_process(c)
        speak(output)

def get_weather(city_name):
    api_key = "your_openweather_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        
        weather_report = f"The temperature in {city_name} is {temperature}°C with {description}."
        print(weather_report)
        speak(weather_report)
    else:
        print(f"City {city_name} not found.")
        speak(f"Sorry, I couldn't find weather data for {city_name}.")



if __name__ == "__main__":
    speak("Initializing Jarvis") 
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5)

                try:
                    word = recognizer.recognize_google(audio)
                    if word.lower() == "jarvis":
                        speak("Yes")
                        print("Jarvis Active...")
                        with sr.Microphone() as source:
                            recognizer.adjust_for_ambient_noise(source)
                            print("Listening for command...")
                            audio = recognizer.listen(source, timeout=10)
                            try:
                                command = recognizer.recognize_google(audio)
                                print(f"Command recognized: {command}")
                                process_command(command)
                            except sr.UnknownValueError:
                                print("Could not understand the command.")
                                speak("Sorry, I did not understand the command.")
                            except sr.RequestError as e:
                                print(f"Could not request results; {e}")
                                speak("Sorry, there was a request error.")
                except sr.UnknownValueError:
                    print("Could not understand the wake word.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                    speak("Sorry, there was a request error.")
        except Exception as e:
            print(f"Error: {e}")
            speak("I'm sorry, something went wrong.")
