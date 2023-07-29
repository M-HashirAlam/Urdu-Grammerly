import re
import joblib

# Load the saved classifier and vectorizer from disk
classifier = joblib.load('no-noun-dis.joblib')
vectorizer = joblib.load('no-noun-disv.joblib')

input_sentence = input('Enter a sentence: ')

# Check if the input contains any digits using regular expression
if re.search(r'\d', input_sentence):
    input_vec = vectorizer.transform([input_sentence])
    prediction = classifier.predict(input_vec)[0]
    if prediction == 'not correct':
        prediction = 'Number-Noun Disagreement'
    print( prediction)
