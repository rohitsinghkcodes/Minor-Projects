import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter the city name: ")
api_url = f"http://api.weatherapi.com/v1/current.json?key=4b56c9ae377f4b5297a105555230505&q={city}"

try:
    res = requests.get(api_url)
    dic_res = json.loads(res.text)

    temp = dic_res["current"]["temp_c"]
    txt = f"The temperature in {city} is {temp} degree celcius"
    print(txt)
    engine.say(txt)
    engine.runAndWait()
except Exception as e:
    print(f"Error! : {e} ")