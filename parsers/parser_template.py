from __future__ import unicode_literals
import spacy
import sys
from random import choice, shuffle

nlp = spacy.load('en')

text = open("./parsers/templates/05.txt").read().decode('utf-8') #NOTe: path is relative to root
doc = nlp(text)
print text
for item in doc:
  # print item.text, item.pos_, item.tag_
  print item.tag_
