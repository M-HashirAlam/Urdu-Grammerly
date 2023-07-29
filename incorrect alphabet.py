import Levenshtein
from Levenshtein import distance as lev

name = input("Enter a word: ")
input_sentence = name.strip().rstrip('.')
sentence_endings = ['۔', '.', '!', '?']
for ending in sentence_endings:
    if input_sentence.endswith(ending):
        input_sentence = input_sentence[:-1]
f = open('wordlist.txt', "r+", encoding="utf-8")
x = f.read()

a = input_sentence.split(' ')  # for whole line to convert into a single word

for word in a:
    if word not in x:
        distances = {key: lev(word, key) for key in x.split()}  # distance formula
        result = {key: value for (key, value) in distances.items() if value <= 1}  # to find closest word

        print(word + " is an incorrect word")
        print("Here are some suggestions:")
        print(result)

        # Find the position and incorrect letter
        if result:
            correct_word = next(iter(result))
            for i in range(min(len(word), len(correct_word))):
                if word[i] != correct_word[i]:
                    print("The incorrect letter is", word[i], "at position:", i)
                    break
            else:
                if len(word) < len(correct_word):
                    print("The incorrect letter is", correct_word[len(word)], "at position:", len(word))
                elif len(correct_word) < len(word):
                    print("The incorrect letter is", word[len(correct_word)], "at position:", len(correct_word))

