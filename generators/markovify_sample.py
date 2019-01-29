# encoding=utf8
from __future__ import unicode_literals
import markovify
import spacy
import sys
import configparser
import requests
from random import choice, shuffle
import json
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

# Get raw text as string.
with open("./compiled_source/samples04.txt") as f:
    text = f.read()

def get_weather_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweatherapi']['api']

def get_guardian_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['theguardian']['api']

def get_news_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['newsapi']['api']

def get_location_from_ip():
    ip_address = sys.argv[1]
    url = 'http://ipinfo.io/{}'.format(ip_address)
    r = requests.get(url)
    payload = r.json()
    IP=payload['ip']
    city = payload['city']
    country=payload['country']
    region=payload['region']
    # print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP)
    return payload

# Build the model.
text_model = markovify.Text(text)

def rant_first():
    tmp_chain = list()
    tmp_chain.append(text_model.make_sentence())
    for i in range(2):
        tmp_chain.append(text_model.make_short_sentence(140))

    # tmp_chain.append(text_model.make_sentence())
    # tmp_chain.append(text_model.make_short_sentence(140))
    mm_chain = [s.decode('unicode_escape').encode('utf8') for s in tmp_chain]
    blurb = ' '.join(mm_chain)

    return blurb

# ## parsed markovify chain with spacy for Entities and Adjectives
nlp = spacy.load('en_core_web_md')

def parse_blurb(blurb):
    doc = nlp(blurb)
    entities = [item.text for item in doc.ents]
    noun_phrase = [item.text.strip() for item in doc.noun_chunks if len(item.text.split(' ')) > 1]
    adjectives = [item.text for item in doc if item.pos_ == 'ADJ']
    return {"entities": entities, "noun_phrase" : noun_phrase, "adjectives": adjectives}


def get_weather(location):
    api_key = get_weather_api_key()
    latlng = location.split(',')
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(latlng[0], latlng[1], api_key)
    r = requests.get(url)
    payload = r.json()
    main = payload['weather'][0]['main']
    description = payload['weather'][0]['description']
    return {"main": main, "description": description}

def get_headline():
    api_key = get_news_api_key()
    sources = ["al-jazeera-english","new-scientist","associated-press","buzzfeed","the-hindu","wired","national-geographic","reddit-r-all","australian-financial-review","google-news","the-wall-street-journal","the-new-york-times","the-guardian-uk"]
    rand_source = choice(sources)
    url = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}".format(rand_source, api_key)
    r = requests.get(url)
    payload = r.json()
    articles = payload['articles']
    article = choice(articles)

    if(rand_source == "reddit-r-all"):
        article_title = article["title"]
        tmp_model = parse_blurb(article_title)
    else:
        description = article["description"]
        tmp_model = parse_blurb(description)
    return tmp_model["noun_phrase"]

def swap_outputs(location, weather, headline_terms, snippet):
    print(weather)
    print(headline_terms)
    print(snippet)
    parsed_sample = parse_blurb(snippet)
    old_noun_phrase = choice(parsed_sample["noun_phrase"])
    new_noun_phrase = choice(headline_terms)
    old_adjective = choice(parsed_sample["adjectives"])
    old_adjective_2 = choice(parsed_sample["adjectives"])
    old_entities = choice(parsed_sample["entities"])
    new_chunk = snippet.replace(old_noun_phrase, new_noun_phrase).replace(old_adjective, weather["description"]).replace(old_adjective_2, weather["main"]).replace(old_entities, location["region"])
    print(new_chunk)



if __name__ == '__main__':
    location = get_location_from_ip()
    weather_prediction = get_weather(location['loc'])
    headline_terms = get_headline()
    markov_snippet = rant_first()
    swap_outputs(location, weather_prediction, headline_terms, markov_snippet)
