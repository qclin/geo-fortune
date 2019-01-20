# coding: utf-8
#if doesn't work in terminal, type following commands
#export LC_ALL=en_US.UTF-8
#export LANG=en_US.UTF-8

from __future__ import unicode_literals
import spacy
import sys
import datetime
from random import choice, shuffle
import json

nlp = spacy.load('en_core_web_md')
text = open("./samples/Theory_of_the_Earth.txt", 'rb').read().decode('utf-8', errors='replace') #NOTe: path is relative to root
doc = nlp(text)

adverbs = [item.text for item in doc if item.pos_ == 'ADV']

entities = [item.text for item in doc.ents]
# for item in doc.noun_chunks:
#     print len(item.text.split(' '))

def flatten_subtree(st):
    return ''.join([w.text_with_ws for w in list(st)]).strip()

noun_phrase = [item.text.strip() for item in doc.noun_chunks if len(item.text.split(' ')) > 1]

subjects = []
for word in doc:
    if word.dep_ in ('nsubj', 'nsubjpass'):
        subjects.append(flatten_subtree(word.subtree))


prep_phrases = []
for word in doc:
    if word.dep_ == 'prep':
        prep_phrases.append(flatten_subtree(word.subtree))

verbs_non_modal = []

for item in doc:
    if item.pos_ == 'VERB':
      # print item.text, item.tag_
      if item.tag_ == 'MD':
        #   do nothing
        string = "useless"
      else:
        verbs_non_modal.append(item.text)


affix = [item.text for item in doc if item.tag_ == 'AFX']
auxiliary_be = [item.text for item in doc if item.tag_ == 'BES']
conjunction_coordinating= [item.text for item in doc if item.tag_ == 'CC']
cardinal_number = [item.text for item in doc if item.tag_ == 'CD']
determiner = [item.text for item in doc if item.tag_ == 'DT']

existential_there = [item.text for item in doc if item.tag_ == 'EX']
foreign_word = [item.text for item in doc if item.tag_ == 'FW']
forms_of_have = [item.text for item in doc if item.tag_ == 'HVS']

conjunction_sub_pre = [item.text for item in doc if item.tag_ == 'IN']
adjective_base = [item.text for item in doc if item.tag_ == 'JJ']
adjective_comparative = [item.text for item in doc if item.tag_ == 'JJR']
adjective_superlative = [item.text for item in doc if item.tag_ == 'JJS']

verbs_modal = [item.text for item in doc if item.tag_ == 'MD']

noun_singular = [item.text for item in doc if item.tag_ == 'NN']
noun_proper_singular = [item.text for item in doc if item.tag_ == 'NNP']
noun_proper_plural = [item.text for item in doc if item.tag_ == 'NNPS']
noun_plural = [item.text for item in doc if item.tag_ == 'NNS']

predeterminer = [item.text for item in doc if item.tag_ == 'PDT']
pronoun_personal = [item.text for item in doc if item.tag_ == 'PRP']
pronoun_possessive = [item.text for item in doc if item.tag_ == 'PRP$']

verb_base = [item.text for item in doc if item.tag_ == 'VB']
verb_singular_third_present = [item.text for item in doc if item.tag_ == 'VBZ']
verb_non_third_present = [item.text for item in doc if item.tag_ == 'VBP']
verb_past = [item.text for item in doc if item.tag_ == 'VBD']
verb_gerunds = [item.text for item in doc if item.tag_ == 'VBG']
verb_past_participle = [item.text for item in doc if item.tag_ == 'VBN']

infinitival_to = [item.text for item in doc if item.tag_ == 'TO']
existential_there = [item.text for item in doc if item.tag_ == 'EX']
conjunction_coor = [item.text for item in doc if item.tag_ == 'CC']

wh_determiner = [item.text for item in doc if item.tag_ == 'WDT']
wh_pronoun_personal = [item.text for item in doc if item.tag_ == 'WP']
wh_pronoun_possessive = [item.text for item in doc if item.tag_ == 'WP$']
wh_adverb = [item.text for item in doc if item.tag_ == 'WRB']

tag_json = {
    "adverbs": adverbs, "verbs_non_modal": verbs_non_modal, "prep_phrases": prep_phrases,
    "subjects": subjects,  "noun_phrase": noun_phrase, "entities": entities,
    "affix": affix, "auxiliary_be": auxiliary_be, "conjunction_coordinating": conjunction_coordinating, "cardinal_number": cardinal_number, "determiner": determiner,
    "existential_there": existential_there, "foreign_word": foreign_word, "forms_of_have": forms_of_have,
    "conjunction_sub_pre" : conjunction_sub_pre, "adjective_base": adjective_base, "adjective_comparative": adjective_comparative, "adjective_superlative": adjective_superlative,
    "verbs_modal": verbs_modal, "noun_singular": noun_singular, "noun_proper_singular": noun_proper_singular, "noun_proper_plural": noun_proper_plural, "noun_plural": noun_plural,
    "predeterminer": predeterminer, "pronoun_possessive" :pronoun_possessive , "pronoun_personal" :pronoun_personal,
    "verb_base": verb_base, "verb_singular_third_present": verb_singular_third_present, "verb_non_third_present": verb_non_third_present, "verb_past": verb_past, "verb_gerunds": verb_gerunds, "verb_past_participle": verb_past_participle,
    "infinitival_to": infinitival_to, "existential_there": existential_there, "conjunction_coor": conjunction_coor,
    "wh_determiner": wh_determiner, "wh_pronoun_personal": wh_pronoun_personal, "wh_pronoun_possessive": wh_pronoun_possessive, "wh_adverb": wh_adverb
}


with open('tag_json_Theory_of_the_Earth.txt', 'w') as outfile:
    json.dump(tag_json, outfile)
