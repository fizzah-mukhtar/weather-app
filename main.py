import requests
import json 
import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    city = input("Enter your city name: ")
    url = f"https://api.weatherapi.com/v1/current.json?key=063be6719a2c40bdb06105738232507&q={city}"
    r = requests.get(url)
    print(r.text)
    dict = json.loads(r.text)
    w = dict["current"]["temp_c"]
    engine.say(w)
    engine.runAndWait()
    
    