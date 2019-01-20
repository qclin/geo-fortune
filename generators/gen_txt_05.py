import json
from random import choice, shuffle

with open('./parsed_sample/tag_json_deborah_coen_climate_in_motion.txt') as json_file: # path relative to root
    data = json.load(json_file)

# pronoun_personal or subjects
PRP_1 = 'we'
PRP_2 = 'it'
PRP_3 = 'me'
PRP_4 = 'ourselves'

#determiner
DT_1 = 'the'
DT_2 = 'no'
DT_3 = 'those'
DT_4 = 'all'
DT_5 = 'an'
DT_6 = 'each'
DT_7 = 'any'
DT_8 = 'this'

# verb_past
VBD_1 = 'were'
VBD_2 = 'gave'
VBD_3 = 'had'
VBD_4 = 'was'
VBD_5 = 'did'

# adjective_base
JJ_1 = 'other'

# conjunction_sub_pre
IN_1 = 'of'
IN_2 = 'at'
IN_3 = 'to'

# conjunction_coordinating
cc_1 = 'and'

time_json = json.loads(open("./corporas/temporal.json").read())
time_formal = time_json['formal']
time_informal = time_json['informal']
time_relative = time_json['relative']

time_informal_plural_1 = choice(time_formal) + 's'

unit_json = json.loads(open("./corporas/units.json").read())
units_long = unit_json['long']

weather_json = json.loads(open("./corporas/weather_conditions.json").read())
weather_conditions = weather_json['conditions']

setting_json = json.loads(open("./corporas/setting.json").read())
settings = setting_json['settings']
place = choice(settings)
place_name = place['name']
place_syn = place['synonyms']

place_1 = choice(settings)
place_name_1 = place['name']
place_syn_1 = place['synonyms']

# Those were the days, when we were all at sea.
def gen_sentence_a():
    return ' '.join([DT_3, VBD_1, DT_1, time_informal_plural_1, ',', choice(data["wh_adverb"]), PRP_1, VBD_1, DT_4, IN_2, place_name])

# It seems like yesterday to me.
def gen_sentence_b():
    return ' '.join([PRP_2, choice(data["verb_singular_third_present"]) , choice(data["conjunction_sub_pre"]), choice(time_informal), choice(data["conjunction_sub_pre"]), PRP_3])

# Species, sex, race, class: in those days none of this meant anything at all.
def gen_sentence_c():
    return ' '.join([choice(data["noun_plural"]) , choice(data["noun_singular"]) , choice(data["noun_singular"]) , choice(data["noun_singular"]) , " : ", choice(data["conjunction_sub_pre"]), DT_3, time_informal_plural_1, choice(data["noun_singular"]) , IN_1, DT_3, choice(data["verb_past_participle"]) , choice(data["noun_singular"]), IN_2, choice(data["adverbs"])])

# No parents, no children, just ourselves, strings of inseparable sisters,
def gen_sentence_d():
    return ' '.join([ DT_2, choice(data["noun_plural"]) ,", ", DT_2, choice(data["noun_plural"]) , ", ", choice(data["adverbs"]), PRP_4, ", ", choice(data["noun_plural"]) , IN_1, choice(data["adjective_base"]) , choice(data["noun_plural"]) , ", "])

# warm and wet, indistinguishable one from the other, gloriously indiscriminate, promiscuous and fused.
def gen_sentence_e():
    return ' '.join([choice(weather_conditions), cc_1, choice(weather_conditions), ", ", choice(data["adjective_base"]), choice(data["cardinal_number"]) , choice(data["conjunction_sub_pre"]), DT_1, JJ_1, ", ", choice(data["adverbs"]), choice(data["adjective_base"]), ", ", choice(data["adjective_base"]), cc_1, choice(data["adjective_base"])])

# No generations.
def gen_sentence_f():
    return ' '.join([DT_2, choice(data["noun_plural"])])
# No future, no past.
def gen_sentence_g():
    return ' '.join([DT_2, choice(time_informal), ",", DT_2, choice(time_informal)])

def gen_sentence_h():
    # An endless geographic plane of micromeshing pulsing quanta,
    h1 = ' '.join([ DT_5, choice(data["adjective_base"]) , choice(data["adjective_base"]) , choice(data["noun_singular"]), IN_1, choice(data["verb_gerunds"]), choice(data["verb_gerunds"]), choice(data["noun_singular"]), ", "])
    # limidess webs of interacting blendings, leakings, mergings,
    h2 = ' '.join([choice(data["adjective_base"]) , choice(data["noun_singular"]),  IN_1, choice(data["verb_gerunds"]), choice(data["verb_gerunds"]) +'s,', choice(data["verb_gerunds"]) +'s,', choice(data["verb_gerunds"]) +'s,'])
    # weaving through ourselves, running rings around each other,
    h3 = ' '.join([choice(data["verb_gerunds"]), choice(data["conjunction_sub_pre"]), PRP_4, ', ', choice(data["verb_gerunds"]), choice(data["noun_plural"]) , choice(data["conjunction_sub_pre"]), DT_6, JJ_1, ', '])
    # heedless, needless, aimless, careless, thoughdess, amok.
    h4 = ', '.join([choice(data["adjective_base"])  , choice(data["adjective_base"])  , choice(data["adjective_base"])  , choice(data["adjective_base"])  , choice(data["noun_singular"]) ,choice(data["adverbs"])])
    return h1 + h2 + h3 + h4

# Folds and foldings,
# plying and multiplying,
# plicatirig and replicating.
def gen_sentence_i():
    return ', '.join([choice(data["noun_plural"]), cc_1, choice(data["verb_gerunds"]), ',', choice(data["verb_gerunds"]), cc_1, choice(data["verb_gerunds"]), ',', choice(data["verb_gerunds"]), cc_1, choice(data["verb_gerunds"])])

# We had no definition,
# no meaning,
# no way of telling each other apart.
def gen_sentence_j():
    return ' '.join([PRP_1, VBD_3, DT_2, choice(data["noun_singular"]), ',', DT_2, choice(data["verb_gerunds"]), ',', DT_2, choice(data["noun_singular"]), IN_1, choice(data["verb_gerunds"]), DT_6, JJ_1, choice(data["adverbs"])])


# We were whatever we were up to at the time.
def gen_sentence_k():
    return ' '.join([PRP_1, VBD_1, choice(data["wh_determiner"]), PRP_1, VBD_1, choice(data["conjunction_sub_pre"]), choice(data["conjunction_sub_pre"]), IN_2, DT_1, choice(time_informal)])


def gen_sentence_l():
    # Free exchanges, microprocesses finely tuned,
    l1 =  ' '.join([choice(data["adjective_base"]) ,choice(data["noun_plural"]), ',' , choice(data["noun_plural"]), choice(data["adverbs"]), choice(data["verb_past_participle"]), ','])
    # polymorphous transfers without regard for borders and boundaries.
    l2 = ' '.join([choice(data["adjective_base"]) , choice(data["noun_plural"]), choice(data["conjunction_sub_pre"]), choice(data["noun_singular"]), choice(data["conjunction_sub_pre"]), choice(place_syn_1), cc_1, choice(place_syn_1)])
    return l1 + l2

def gen_sentence_m():
     # There was nothing to hang on to,
    m1 = ' '.join([choice(data["existential_there"]), VBD_4, choice(data["subjects"]), "to", choice(data["verb_base"]), choice(data["conjunction_sub_pre"]), IN_3, ","])
    # nothing to be grasped,
    m2 = ' '.join([choice(data["subjects"]), "to", choice(data["verb_base"]), choice(data["verb_past_participle"]), ','])
    # nothing to protect or be protected from.
    m3 = ' '.join([choice(data["subjects"]), "to", choice(data["verb_base"]), choice(data["conjunction_coor"]), choice(data["verb_base"]), choice(data["verb_past_participle"]), choice(data["conjunction_sub_pre"])])
    return m1 + m2 + m3


def gen_sentence_n():
# Insides and outsides did not count.
    return ' '.join([choice(place_syn), cc_1, choice(place_syn), VBD_5, choice(data["adverbs"]), choice(data["verb_base"])])

def gen_sentence_o():
# We gave no thought to any such things.
    return ' '.join([PRP_1, VBD_2, DT_2, choice(data["noun_singular"]), choice(data["conjunction_sub_pre"]), DT_7, choice(data["adjective_base"]) , choice(data["noun_plural"])])

def gen_sentence_p():
# We gave no thought to anything at all.
    return ' '.join([PRP_1, VBD_2, DT_2, choice(data["noun_singular"]), IN_1, choice(data["noun_singular"]), IN_3, choice(data["adverbs"])])

def gen_sentence_q():
# Everything was there for the taking then.
    return ' '.join([choice(data["noun_singular"]), VBD_4, choice(data["adverbs"]), choice(data["conjunction_sub_pre"]), DT_1, choice(data["noun_singular"]), choice(data["adverbs"])])

def gen_sentence_r():
# We paid no attention: it was all for free.
    return ' '.join([PRP_1, choice(data["verb_past"]), DT_2, choice(data["noun_singular"]), " : ", PRP_2, VBD_4, DT_4, choice(data["conjunction_sub_pre"]), choice(data["adjective_base"]) ])

# It had been this way for tens, thousands, millions, billions of what were later defined as years.
def gen_sentence_s():
    return ' '.join([PRP_2, VBD_3, choice(data["verb_past_participle"]), DT_8, choice(data["noun_singular"]), IN_1, choice(units_long), choice(units_long), choice(units_long), choice(units_long), choice(data["conjunction_sub_pre"]), choice(data["wh_pronoun_personal"]), choice(time_informal), choice(data["adverbs"]), choice(data["verb_past_participle"]), choice(data["conjunction_sub_pre"]), choice(time_informal) +'s'])

# If we had thought about it, we would have said it would go on forever, this fluent, fluid world.
def gen_sentence_t():
    return ' '.join([choice(data["conjunction_sub_pre"]), PRP_1, VBD_3, choice(data["verb_past_participle"]), choice(data["conjunction_sub_pre"]), PRP_2, ',', PRP_1,  choice(data["verbs_modal"]), choice(data["verb_base"]), choice(data["verb_past_participle"]), PRP_2, choice(data["verbs_modal"]), choice(data["verb_base"]), choice(data["adverbs"]), choice(data["adverbs"]), DT_8, choice(data["adjective_base"]), choice(data["adjective_base"]), place_name_1])



print gen_sentence_a()
print gen_sentence_b()
print gen_sentence_c()
print gen_sentence_d()
print gen_sentence_e()
print gen_sentence_f()
print gen_sentence_g()
print gen_sentence_h()
print gen_sentence_i()
print gen_sentence_j()
print gen_sentence_k()
print gen_sentence_l()
print gen_sentence_m()
print gen_sentence_n()
print gen_sentence_o()
print gen_sentence_p()
print gen_sentence_q()
print gen_sentence_r()
print gen_sentence_s()
print gen_sentence_t()
