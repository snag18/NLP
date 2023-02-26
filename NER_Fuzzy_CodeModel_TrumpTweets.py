
from collections import Counter
import spacy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import en_core_web_sm

# in the terminal
# pip install spacy
# pip install python-Levenshtein
# pip install python -m spacy en_core_web_sm OR
# python -m spacy download en
# opens in Spyder or PyCharm

# if the text is in English use this
nlp = spacy.load('en')

with open("/Users/sayali/Desktop/Columbia/QMSS/RA ISERP/Data/Trump_Tweets_All.txt") as file:
    text = file.read()

n = nlp(text) # nlp is the name of the code that runs spacy's english language model
3
create_text = [(X.text, X.label_) for X in n.ents] # creates specific text words and their labels based on different categories

create_label = [x.label_ for x in n.ents] # generates NER label for each quantity in b

category_no = Counter(create_label) # output gives the number of terms in each NER category

entity = [x.text for x in n.ents] # generates actual entities in above categories

entity_no = Counter(entity) # allows us to find the exact number of times an entity occured

people = [] # empty list where entities from one category can be added for a further fuzzy matching process
for x in create_text:
   if x[1] == 'PERSON':
        people.append(x[0])
uniq_ppl = set(people)

organizations = []
for x in create_text:
  if x[1] == 'ORG':
      organizations.append(x[0])
uniq_orgs = set(organizations)

places = []
for x in create_text:
   if x[1] == 'GPE':
        places.append(x[0])
uniq_plc = set(places)

groups = []
for x in create_text:
   if x[1] == 'NORP':
        groups.append(x[0])
uniq_grp = set(groups)

dates = []
for x in create_text:
    if x[1] == 'DATE':
         dates.append(x[0])
uniq_dts = set(dates)

money = []
for x in create_text:
   if x[1] == 'MONEY':
        money.append(x[0])
uniq_mny = set(money)

art = []
for x in create_text:
    if x[1] == 'WORK_OF_ART':
        art.append(x[0])
uniq_art = set(art)

# fuzzy matching process for specific entities in above-mentioned categories
# fuzz.ratio - compares names of entities
# fuzz.partial_ratio - measures specific characters
# fuzz.token_set_ratio - sorts alphabetically and removes stop words
# finds matches of the key word in the same category list or another category list
# no indicates matches found

interest_word_a = process.extract("a", uniq_ppl, limit=100, scorer=fuzz.ratio)

interest_word_b = process.extract("b", uniq_plc, limit=100, scorer=fuzz.partial_ratio)

interest_word_c = process.extract("c", uniq_orgs, limit=100, scorer=fuzz.token_set_ratio)

interest_word_latinos = process.extract("Latinos", uniq_ppl, limit=100, scorer=fuzz.ratio)

interest_word_latinos = process.extract("Latinos", uniq_mny, limit=100, scorer=fuzz.ratio)

interest_word_latinos = process.extract("Latinos", uniq_art, limit=100, scorer=fuzz.ratio)

interest_word_mex = process.extract("Mexican", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_mex = process.extract("Mexican", uniq_mny, limit=100, scorer=fuzz.ratio)

interest_word_hisp = process.extract("Hispanic", uniq_ppl, limit=100, scorer=fuzz.ratio)

interest_word_hisp = process.extract("Hispanic", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_hisp = process.extract("Hispanic", uniq_grp, limit=100, scorer=fuzz.ratio)

interest_word_illegal = process.extract("illegal", uniq_ppl, limit=100, scorer=fuzz.ratio)

interest_word_illegal = process.extract("illegal", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_illegal = process.extract("illegal", uniq_grp, limit=100, scorer=fuzz.ratio)

interest_word_illegal = process.extract("illegals", uniq_mny, limit=100, scorer=fuzz.ratio)

interest_word_illegal = process.extract("illegals", uniq_art, limit=100, scorer=fuzz.ratio)

interest_word_undoc = process.extract("undocumented", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_undoc = process.extract("undocumented", uniq_grp, limit=100, scorer=fuzz.ratio)

interest_word_undoc = process.extract("undocumented", uniq_art, limit=100, scorer=fuzz.ratio)

interest_word_PR = process.extract("Puerto Rico", uniq_ppl, limit=100, scorer=fuzz.ratio)

interest_word_PR = process.extract("Puerto Rico", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_PR = process.extract("Puerto Rico", uniq_grp, limit=100, scorer=fuzz.ratio)

interest_word_alien = process.extract("aliens", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_alien = process.extract("aliens", uniq_mny, limit=100, scorer=fuzz.ratio)

interest_word_immg = process.extract("illegal immigration", uniq_ppl, limit=100, scorer=fuzz.ratio)

interest_word_immg = process.extract("illegal immigration", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_immg = process.extract("illegal immigration", uniq_grp, limit=100, scorer=fuzz.ratio)

interest_word_immg = process.extract("illegal immigration", uniq_plc, limit=100, scorer=fuzz.ratio)

interest_word_mig = process.extract("migrants", uniq_ppl, limit=100, scorer=fuzz.ratio)

interest_word_mig = process.extract("migrants", uniq_grp, limit=100, scorer=fuzz.ratio)

interest_word_mig = process.extract("migrants", uniq_mny, limit=100, scorer=fuzz.ratio)

interest_word_car = process.extract("caravan", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_car = process.extract("caravan", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_car = process.extract("caravan", uniq_mny, limit=100, scorer=fuzz.ratio)

interest_word_inv = process.extract("invasion", uniq_ppl, limit=100, scorer=fuzz.ratio)

interest_word_inv = process.extract("invasion", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_inv = process.extract("invasion", uniq_grp, limit=100, scorer=fuzz.ratio)

interest_word_inf = process.extract("infestation", uniq_orgs, limit=100, scorer=fuzz.ratio)

interest_word_inf = process.extract("infestation", uniq_mny, limit=100, scorer=fuzz.ratio)

interest_word_border = process.extract("border", uniq_grp, limit=100, scorer=fuzz.ratio)

interest_word_rapist = process.extract("rapist", uniq_orgs, limit=100, scorer=fuzz.ratio)
