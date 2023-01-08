import requests
import json


class Horoscope:
    def __init__(self, sign):
        self.sign = sign.lower()
        self.astro_data = {} 
    def get_horoscope(self):
        url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
        querystring = {"sign":self.sign,"day":"today"}
        headers = {
	      "X-RapidAPI-Key": "43b2e52da3msh46b3b1e9fb62784p135409jsn9c7ea8f93068",
	      "X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
           }
        response = requests.request("POST", url, headers=headers, params=querystring)
        self.astro_data = json.loads(response.text)


response = input("Hello! Would you like your horoscope for today? (y,n) ")
if response not in ['yes', 'Yes', 'y', 'Y']:
    print("Ok. Maybe another time.")
else:
    sign = input("Great! What is your sign? ")
    appropriate_signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn",
                         "aquarius", "pisces"]
    if sign.lower() in appropriate_signs:
        player = Horoscope(sign)
        player.get_horoscope()
        print()
        print("For {}:".format(player.astro_data["current_date"]))
        print("Info: {}".format(player.astro_data["description"]))
        print("Compatibility: {}".format(player.astro_data["compatibility"]))
        print("Mood: {}".format(player.astro_data["mood"]))
        print("Color: {}".format(player.astro_data["color"]))
        print("Lucky Number: {}".format(player.astro_data["lucky_number"]))
        print("Lucky Time: {}".format(player.astro_data["lucky_time"]))
    else:
        print("Sorry. You may have a typo.")
        
