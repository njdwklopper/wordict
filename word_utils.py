import json
import random


def get_word_list_by_length(tot):
    file_list_words = open("output/word_data.json", "r")
    dict_words_data = json.loads(file_list_words.read())
    list_words = []
    for word in dict_words_data['words']:
        if len(word['word']) is tot:
            list_words.append(word)
    return list_words


def get_random_word(list_words):
    random_word = list_words[random.randint(0, len(list_words))]
    return random_word['word']
