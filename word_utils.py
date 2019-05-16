import json
import random
import re

from constants import MINIMUM_WORD_LENGTH, MAXIMUM_WORD_LENGTH


def get_dict_words_by_length(tot):
    file_list_words = open("output/word_data.json", "r")
    dict_words_data = json.loads(file_list_words.read())
    list_words = []
    for word in dict_words_data['words']:
        if len(word['word']) is tot:
            list_words.append(word)
    return list_words


# Create list that only contains @total characters per word
def get_list_words_by_length(total):
    file_list_words = open("output/word_data.json", "r")
    dict_words_data = json.loads(file_list_words.read())
    list_words = []
    for word in dict_words_data['words']:
        if len(word['word']) is total:
            list_words.append(word['word'])
    return list_words


# Get words from dictionary, at given lengths that van be used within chosen word
def get_list_words_by_word(word_chosen):
    list_words_tmp = []
    for i in range(MINIMUM_WORD_LENGTH, MAXIMUM_WORD_LENGTH):
        list_words = get_list_words_by_length(i)
        for word in list_words:
            match_count = len(word)
            word_select = word_chosen
            for char in sorted(word):
                if char in word_select:
                    word_select = re.sub(char, '', word_select)
                    match_count -= 1
            if match_count is 0:
                list_words_tmp.append(word)
    return list_words_tmp


def get_random_word(list_words):
    random_word = list_words[random.randint(0, len(list_words))]
    return random_word
