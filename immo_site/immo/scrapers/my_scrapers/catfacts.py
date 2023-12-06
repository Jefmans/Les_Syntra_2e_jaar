import requests
import json 



def get_cat_fact():
    url = "https://cat-fact.herokuapp.com/facts/random/"
    r = requests.get(url)

    data  = json.loads(r.text)

    return data['text']
