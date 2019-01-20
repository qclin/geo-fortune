import json
from random import choice, shuffle

with open('./parsed_sample/tag_json_deborah_coen_climate_in_motion.txt') as json_file: # path relative to root
    data = json.load(json_file)

# What NOUN WP
# we PRON PRP
# must VERB MD
# accept VERB VB

def gen_sentence_a():
    return ' '.join([choice(data["wh_pronoun_personal"]), choice(data["pronoun_personal"]), choice(data["verbs_modal"]), choice(data["verb_base"])])

# SPACE
# As ADP IN
# we PRON PRP
# journey VERB VBP
# through ADP IN
# the DET DT
# world NOUN NN
#
def gen_sentence_b():
    return ' '.join([choice(data["conjunction_sub_pre"]), choice(data["pronoun_personal"]), choice(data["verb_non_third_present"]), choice(data["conjunction_sub_pre"]), choice(data["determiner"]), choice(data["noun_singular"])])


# SPACE
# Is VERB VBZ
# that DET DT
# time NOUN NN
# will VERB MD
# pass VERB VB
# like ADP IN
# the DET DT
# waters NOUN NNS
# of ADP IN
# a DET DT
# stream NOUN NN
# ; PUNCT :


def gen_sentence_c():
    return ' '.join([choice(data["verb_singular_third_present"]), choice(data["determiner"]), choice(data["noun_singular"]), choice(data["verbs_modal"]), choice(data["verb_base"]), choice(data["conjunction_sub_pre"]), choice(data["determiner"]), choice(data["noun_plural"]), choice(data["conjunction_sub_pre"]), choice(data["determiner"]), choice(data["noun_singular"])])

# SPACE
# In ADP IN
# countless ADJ JJ
# numbers NOUN NNS
# , PUNCT ,


# SPACE
# In ADP IN
# relentless ADJ JJ
# succession NOUN NN
# , PUNCT ,

def gen_sentence_d():
    return ' '.join([choice(data["conjunction_sub_pre"]), choice(data["adjective_base"]), choice(data["noun_plural"])])

def gen_sentence_dd():
    return ' '.join([choice(data["conjunction_sub_pre"]), choice(data["adjective_base"]), choice(data["noun_singular"])])

# SPACE
# It PRON PRP
# will VERB MD
# besiege VERB VB
# us PRON PRP

def gen_sentence_e():
    return ' '.join([choice(data["pronoun_personal"]), choice(data["verbs_modal"]), choice(data["verb_base"]), choice(data["pronoun_personal"])])

# SPACE
# With ADP IN
# assaults NOUN NNS
# we PRON PRP
# must VERB MD
# endure VERB VB
# . PUNCT .
#
# SPACE

def gen_sentence_f():
    return ' '.join([choice(data["conjunction_sub_pre"]), choice(data["noun_plural"]), choice(data["pronoun_personal"]), choice(data["verbs_modal"]), choice(data["verb_base"])])



print gen_sentence_a()
print gen_sentence_b()
print gen_sentence_c()
print gen_sentence_d()
print gen_sentence_dd()
print gen_sentence_e()
print gen_sentence_f()
