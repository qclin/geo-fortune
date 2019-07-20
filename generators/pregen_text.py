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

# Get raw text as string.
with open("./compiled_source/samples04.txt") as f:
    text = f.read()


# Build the model.
text_model = markovify.Text(text)

def rant_first():
    tmp_chain = list()
    tmp_chain.append(text_model.make_sentence())
    for i in range(2):
        tmp_chain.append(text_model.make_short_sentence(140))

    # tmp_chain.append(text_model.make_sentence())
    # tmp_chain.append(text_model.make_short_sentence(140))
    # mm_chain = [s.decode('unicode_escape').encode('utf8') for s in tmp_chain]
    mm_chain = [s.decode('unicode_escape').encode('ascii', 'ignore') for s in tmp_chain]
    blurb = ' '.join(mm_chain)

    return blurb

# ## parsed markovify chain with spacy for Entities and Adjectives
nlp = spacy.load('en_core_web_sm')

def parse_blurb(blurb):
    doc = nlp(blurb)
    entities = [item.text for item in doc.ents]
    noun_phrase = [item.text.strip() for item in doc.noun_chunks if len(item.text.split(' ')) > 1]
    adjectives = [item.text for item in doc if item.pos_ == 'ADJ']
    return {"entities": entities, "noun_phrase" : noun_phrase, "adjectives": adjectives, "text": blurb}



def build_json():
    markov_snippet = rant_first()
    parsed_sample = parse_blurb(markov_snippet)
    return markov_snippet, parsed_sample

# with open('tag_json_Geo_Fortune.json', 'w') as fortune_json:
#     json.dump(forturn_json, fortuneFeeds)

newTxt = ''
fname = 'output/json/tag_json_Geo_Fortune.json'

with open(fname) as fortune_json:
    feeds = json.load(fortune_json)
    for i in range(0, 1000):
        result = build_json()
        feeds.append(result[1])
        newTxt += result[0] +'\n\r\n\r'
    with open(fname, mode='w') as f:
        f.write(json.dumps(feeds, indent=2))

with open("output/txt/plain_geo_fortune.txt", "a") as txtFile:
    txtFile.write(newTxt)


# with open('tag_json_Geo_Fortune.json', 'w') as fortune_json:
    # json.dump(forturn_json, fortuneFeeds)
