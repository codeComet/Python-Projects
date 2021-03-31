import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import requests


def get_weather():
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city = "Dhaka"
    api_key = "cb421a8136c0d2b244079f62bf03e475"
    url = base_url + "q=" + city + "&units=metric&appid=" + api_key
    response = requests.get(url)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        # humidity = main['humidity']
        # getting the pressure
        # pressure = main['pressure']
        # weather report
        report = data['weather']
        # print(f"{city:-^30}")
        return (
            f"weather for {city}, The Temperature is: {temperature} degree celsius, and overall weather will be {report[0]['description']}")
        # print(f"Humidity: {humidity}")
        # print(f"Pressure: {pressure}")
        # print(f"Weather Report: {report[0]['description']}")


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def user_command():
    command = ""
    try:
        talk("how can i help you")
        with sr.Microphone() as source:
            print("speak now")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace("alexa", "")
                print(command)
    except sr.UnknownValueError:
        talk("Sorry I could not understand what you said")
    except sr.RequestError:
        talk("Sorry I could not process the results at the moment")

    return command


def run_alexa():
    command = user_command()
    print(command)
    if 'play' in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("It's " + time)
    elif 'weather' in command:
        data = get_weather()
        print(data)
        talk(data)


run_alexa()
