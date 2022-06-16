from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_extract_get_determiner():
   # 1. Test the single determiners.
   single_determiners = ["a", "one", "the"]
  
   # 
   # (_) as the variable name for the counting variable.
   for _ in range(4):
      word = get_determiner(1)
      # Verify that the word returned from get_determiner is
      # one of the words in the single_determiners list.
      assert None in ['a', 'one', 'the']
      assert word in single_determiners

      # 2. Test the plural determiners.
      plural_determiners = ["two", "some", "many", "the"]
      # This loop will repeat the statements inside it 4 times.
   for _ in range(4):
      word = get_determiner(2)
      # Verify that the word returned from get_determiner
      # is one of the words in the plural_determiners list.
      assert word in plural_determiners
def test_get_noun():
   # 1. Test the single determiners.
   single_noun = ["bird", "boy", "car", "cat", "child",
   "dog", "girl", "man", "rabbit", "woman"]

   # This loop will repeat the statements inside it 4 times.
   # If a loop's counting variable is not used inside the
   # body of the loop, many programmers will use underscore
   # (_) as the variable name for the counting variable.
   for _ in range(4):
      word = get_noun(1)
      # Verify that the word returned from get_determiner is
      # one of the words in the single_determiners list.
      assert word in single_noun
      # 2. Test the plural determiners.
      plural_noun = ["birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"]
      # This loop will repeat the statements inside it 4 times.
   for _ in range(4):
      word = get_noun(2)
      # Verify that the word returned from get_determiner
      # is one of the words in the plural_determiners list.
      assert word in plural_noun
def test_get_verb():
   past_tense = ["drank", "ate", "grew", "laughed", "thought",
   "ran", "slept", "talked", "walked", "wrote"]
   for _ in range(4):
      word = get_verb(1, 'past')
      assert word in past_tense

   for _ in range(4):
      word = get_verb(2, 'past')
      assert word in past_tense
      present_tense_singular = ["drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"]
   for _ in range(4):
      word = get_verb(1, 'present')
      assert word in present_tense_singular
      present_tense_plural= ["drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"]

   for _ in range(4):
      word = get_verb(2, 'present')
      assert word in present_tense_plural
      future_tense = ["will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"]
   for _ in range(4):
      word = get_verb(1, 'future')
      assert word in future_tense

   for _ in range(4):
      word = get_verb(2, 'future')
      assert word in future_tense
def test_get_preposition():
   prepositions = ["about", "above", "across", "after", "along",
   "around", "at", "before", "behind", "below",
   "beyond", "by", "despite", "except", "for",
   "from", "in", "into", "near", "of",
   "off", "on", "onto", "out", "over",
   "past", "to", "under", "with", "without"]
   for _ in range(4):
      word = get_preposition()
      assert word in prepositions
def test_get_prepositional_phrase():
   prepositions = ["about", "above", "across", "after", "along",
   "around", "at", "before", "behind", "below",
   "beyond", "by", "despite", "except", "for",
   "from", "in", "into", "near", "of",
   "off", "on", "onto", "out", "over",
   "past", "to", "under", "with", "without"]
   single_determiners = ["a", "one", "the"]
   plural_determiners = ["two", "some", "many", "the"]
   single_noun = ["bird", "boy", "car", "cat", "child",
   "dog", "girl", "man", "rabbit", "woman"]

   plural_noun = ["birds", "boys", "cars", "cats", "children",
   "dogs", "girls", "men", "rabbits", "women"]

  
  
   
pytest.main(["-v", "--tb=line", "-rN", __file__])