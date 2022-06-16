import random
# import re
# import itertools 
def main():

    for i in range(6):
     
        determiner = get_determiner(i)
        determ = get_determiner(0)
        noun = get_noun(1)
        verb = get_verb(1, 'present')
        preposition = get_preposition()
        preposition_word = get_prepositional_phrase(1)
        print(f'{determiner} {noun} {verb} {preposition} {determ} {preposition_word}')
def get_determiner(quantity):
    
    if quantity == 1:
        words = ["a", "one", "the", "that"]
    else:
        words = ["two", "some", "many", "the", "these"]
        # Randomly choose and return a determiner.
        word = random.choice(words)
        word_capitalize = word.capitalize()
        return word
def get_noun(quantity):
 
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun
def get_verb(quantity, tense):
    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    if tense == 'present' and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    if tense == 'present' and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        # Randomly choose and return a verb.
    verb = random.choice(words)
    return verb
def get_preposition():
   
    prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return(preposition)
def get_prepositional_phrase(quantity):
    
    if quantity == 1:
        word= ["car", "cup", "pen"]
    else:
        word= ["cars", "cups", "pens"]
        preparation_word = random.choice(word)
        return preparation_word
        
main()