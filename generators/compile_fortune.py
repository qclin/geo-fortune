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
import regex as re

reload(sys)
sys.setdefaultencoding('utf8')

with open('output/json/tag_json_Geo_Fortune.json') as fortune_json:
    feeds = json.load(fortune_json)

def get_api_key(source):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[source]['api']

def get_location_from_ip():
    ip_address = sys.argv[1]
    url = 'http://ipinfo.io/{}'.format(ip_address)
    r = requests.get(url)
    # print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP)
    return r.json()

# ## parsed markovify chain with spacy for Entities and Adjectives
nlp = spacy.load('en_core_web_sm')


def parse_blurb(blurb):
    doc = nlp(blurb)
    entities = [item.text for item in doc.ents]
    noun_phrase = [item.text.strip() for item in doc.noun_chunks if len(item.text.split(' ')) > 1]
    adjectives = [item.text for item in doc if item.pos_ == 'ADJ']
    return {"entities": entities, "noun_phrase" : noun_phrase, "adjectives": adjectives}


def get_weather(location):
    api_key = get_api_key('openweatherapi')
    latlng = location.split(',')
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(latlng[0], latlng[1], api_key)
    r = requests.get(url)
    payload = r.json()
    # main = payload['weather'][0]['main']
    # description = payload['weather'][0]['description']
    return {"weather": payload['weather'][0], "station": payload['name'] }

def get_headline():
    api_key = get_api_key('newsapi')
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


def swap_outputs(location, forecast, headline_terms, snippet_json):
    og_entities = snippet_json["entities"]
    og_nouns = snippet_json["noun_phrase"]
    og_adjectives = snippet_json["adjectives"]
    og_text = snippet_json['text']
    new_chunk = og_text

    if(len(og_entities) > 0):
        og_entity = choice(og_entities)
        new_subject = choice(headline_terms)
        new_chunk = new_chunk.replace(og_entity, new_subject)


    if(len(og_adjectives) > 1):
        og_adjective = choice(og_adjectives)
        og_adjective_2 = choice(og_adjectives)
        new_chunk = new_chunk.replace(og_adjective, forecast["weather"]["description"]).replace(og_adjective_2, forecast["weather"]["main"])

    if(len(og_nouns) > 0):
        # address = location['region'] or location["city"]
        og_noun = choice(og_nouns)
        new_chunk = new_chunk.replace(og_noun, forecast["station"])

    clean_chunk = re.sub(r'[()\"#/@<>{}`+=~|]', ' ', new_chunk)
    print(clean_chunk)


if __name__ == '__main__':
    location = get_location_from_ip()
    weather_prediction = get_weather(location['loc'])
    headline_terms = get_headline()
    swap_outputs(location, weather_prediction, headline_terms, choice(feeds))
