import Levenshtein
import re

def find_closest_words(input_string, word_list):
    closest_words = []
    if re.search(r'\d', input_string):
        # If the input_string contains a digit, return an empty list
        return closest_words

    for word in word_list:
        distance = Levenshtein.distance(input_string, word)
        if distance <= 1:
            closest_words.append({"suggestion": word})
    return closest_words
