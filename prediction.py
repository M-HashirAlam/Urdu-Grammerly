import numpy as np
import string
lexicon = {}


def update_lexicon(current: str, next_word: str) -> None:
    """Add item to the lexicon.
    Args:
        current (str): Input word.
        next_word (str): Output word.
    """

    # Add the input word to the lexicon if it in there yet.
    if current not in lexicon:
        lexicon.update({current: {next_word: 1}})
        return

    # Receive the probabilities of the input word.
    options = lexicon[current]

    # Check if the output word is in the probability list.
    if next_word not in options:
        options.update({next_word: 1})
    else:
        options.update({next_word: options[next_word] + 1})

    # Update the lexicon
    lexicon[current] = options


# Populate lexicon
with open('sentences_data.txt', 'r', encoding="utf-8") as dataset:
    for line in dataset:
        clean_sentence = line.translate(str.maketrans('', '', string.punctuation))
        words = clean_sentence.strip().split(' ')
        for i in range(len(words) - 1):
            update_lexicon(words[i], words[i + 1])

# Adjust probability
for word, transition in lexicon.items():
    transition = dict((key, value / sum(transition.values())) for key, value in transition.items())
    lexicon[word] = transition


# Define function for predicting the next word
def predict_next_word(text):
    words = text.strip().split(' ')
    if words[-1] not in lexicon:
        return 'Word not found'
    else:
        options = lexicon[words[-1]]
        predicted = np.random.choice(list(options.keys()), p=list(options.values()))
        return " " + predicted
