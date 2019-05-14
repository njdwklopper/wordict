# JSON Dictionary and score creator
# Dictionary from https://github.com/dwyl
# Scores from https://github.com/dariusk/corpora

import json
import urllib.request

DICTIONARY_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"
SCRABBLE_SCORE_URL = "https://raw.githubusercontent.com/dariusk/corpora/master/data/games/scrabble.json"
MINIMUM_WORD_LENGTH = 3
MAXIMUM_WORD_LENGTH = 6

words = open("output/words.txt", "w")
with urllib.request.urlopen(DICTIONARY_URL) as url:
    _word_data_ = json.loads(url.read().decode())
    for line in _word_data_:
        if MINIMUM_WORD_LENGTH <= len(line) <= MAXIMUM_WORD_LENGTH:
            words.write(line + "\n")
    words.close()

scores = {}
with urllib.request.urlopen(SCRABBLE_SCORE_URL) as url:
    _score_data_ = json.loads(url.read().decode())
    keylist = _score_data_['letters'].keys()
    for key in keylist:
        print(key)
    # for line in _score_data_['letters']:
    #     print("%s: %d" % (line, _score_data_[line]))

_new_dictionary_data_ = {'words': []}
for word in words:
    _new_dictionary_data_['word'].append({
        'name': word,
        'score': '1',
        'from': 'Nebraska'
    })

with open('output/word_data.json', 'w') as word_data:
    json.dump(_new_dictionary_data_, word_data)
