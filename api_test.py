#{"date_range": "Jan 20 - Feb 18", "current_date": "January 7, 2023", "description": "It doesn't take much persuasion on your part to get a certain someone to see your side of things -- a few well-placed words will take care of that. In fact, your charm is so powerful, it's almost unfair.", "compatibility": "Leo", "mood": "Charming", "color": "Copper", "lucky_number": "42", "lucky_time": "2am"}

import requests
import json
url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

querystring = {"sign":"aquarius","day":"today"}

headers = {
	"X-RapidAPI-Key": "43b2e52da3msh46b3b1e9fb62784p135409jsn9c7ea8f93068",
	"X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
}

response = requests.request("POST", url, headers=headers, params=querystring)

my_dict = json.loads(response.text)

print(type(my_dict))