import requests
import json
import win32com.client
city =input("enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=001af7d257074e77aeb160125231310&q={city}"

r =requests.get(url)
wdic =json.loads(r.text)
w=wdic["current"]["temp_c"]
print(w)
speak =win32com.client.Dispatch("SAPI.SpVoice")
speak.Speak(f"the current weather in {city} is {w} degree celcius")