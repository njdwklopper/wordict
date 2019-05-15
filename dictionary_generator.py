# JSON Dictionary and score creator
# Dictionary from https://github.com/dwyl
# Scores from https://github.com/dariusk/corpora

import json
import urllib.request

DICTIONARY_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"
SCRABBLE_SCORE_URL = "https://raw.githubusercontent.com/dariusk/corpora/master/data/games/scrabble.json"
MINIMUM_WORD_LENGTH = 3
MAXIMUM_WORD_LENGTH = 6

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

file_list_shrunk_words = open("output/words.txt", "w")
with urllib.request.urlopen(DICTIONARY_URL) as url:
    dict_word_data = json.loads(url.read().decode())
    for line in list_shrunk_words:
        file_list_shrunk_words.write(line + "\n")
    file_list_shrunk_words.close()

dict_letter_scores = {}
with urllib.request.urlopen(SCRABBLE_SCORE_URL) as url:
    dict_scores_data = json.loads(url.read().decode())
    for letter, list_data in dict_scores_data['letters'].items():
        if 'points' in dict_scores_data['letters'][letter]:
            dict_letter_scores[letter] = list_data['points']
    print(dict_letter_scores)

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

with open('output/word_data.json', 'w') as word_data:
    json.dump(dict_gen_word_data, word_data)
