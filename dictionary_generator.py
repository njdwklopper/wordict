# Generate Word Dictionary
import json
import urllib.request

from constants import *

list_shrunk_words = []

# Create Word list with minimum and maximum length
with urllib.request.urlopen(DICTIONARY_URL) as url:
    dict_word_data = json.loads(url.read().decode())
    for line in dict_word_data:
        if MINIMUM_WORD_LENGTH <= len(line) <= MAXIMUM_WORD_LENGTH:
            list_shrunk_words.append(line)

# Remove duplicates:
list_shrunk_words = list(dict.fromkeys(list_shrunk_words))
print(list_shrunk_words)

# Create text file from list
file_list_shrunk_words = open("dictionary/words.txt", "w")
with urllib.request.urlopen(DICTIONARY_URL) as url:
    dict_word_data = json.loads(url.read().decode())
    for line in list_shrunk_words:
        file_list_shrunk_words.write(line + "\n")
    file_list_shrunk_words.close()

# Get/map scrabble scores for letters
dict_letter_scores = {}
with urllib.request.urlopen(SCRABBLE_SCORE_URL) as url:
    dict_scores_data = json.loads(url.read().decode())
    for letter, list_data in dict_scores_data['letters'].items():
        if 'points' in dict_scores_data['letters'][letter]:
            dict_letter_scores[letter] = list_data['points']
    print(dict_letter_scores)

# Create Words json dictionary with complete score (work in progress to add other data)
dict_gen_word_data = {'words': []}
for word in list_shrunk_words:
    sum_score = 0
    for letter in word:
        for score in dict_letter_scores.items():
            if letter in score:
                sum_score = sum_score + score[1]
    dict_gen_word_data['words'].append({
        'word': word,
        'score': sum_score
    })
print(dict_gen_word_data)

with open('dictionary/word_data.json', 'w') as word_data:
    json.dump(dict_gen_word_data, word_data)
