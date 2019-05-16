import json
import random
import re

from constants import MINIMUM_WORD_LENGTH, MAXIMUM_WORD_LENGTH


# Create dict that only contains @total characters per word
def get_dict_words_by_length(length, file_list_words):
    dict_words_data = json.loads(file_list_words)
    list_words = []
    for word in dict_words_data:
        if len(word) is length:
            list_words.append(word)
    return list_words


# Create list that only contains @total characters per word
def get_list_words_by_length(length, file_list_words):
    dict_words_data = json.loads(file_list_words)
    list_words = []
    for word in dict_words_data:
        if len(word) is length:
            list_words.append(word)
    return list_words


def get_list_letter_scores(file_list_letter_scores):
    dict_letter_scores = {}
    dict_scores_data = json.loads(file_list_letter_scores)
    for letter, list_data in dict_scores_data['letters'].items():
        if 'points' in dict_scores_data['letters'][letter]:
            dict_letter_scores[letter] = list_data['points']
    return dict_letter_scores


# s
def get_letter_score(letter, file_list_letter_scores):
    return get_list_letter_scores(file_list_letter_scores)[letter]


# s
def get_word_score(word, file_list_words):
    return json.loads(file_list_words)[word]['score']


# Get words from dictionary, at given lengths that can be used from chosen word's chars
def get_list_words_by_word(word_chosen, file_list_words):
    list_words_tmp = []
    for i in range(MINIMUM_WORD_LENGTH, MAXIMUM_WORD_LENGTH):
        list_words = get_list_words_by_length(i, file_list_words)
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


# Generate a Single Game Level Dictionary from an index
def get_game_level(index, file_list_words):
    list_words_index_ = get_dict_words_by_length(MAXIMUM_WORD_LENGTH, file_list_words)[index]
    selected_word = list_words_index_
    dict_tmp = {}
    list_anagrams = get_list_words_by_word(selected_word, file_list_words)
    for word in list_anagrams:
        dict_tmp[word] = {"word": word, "score": get_word_score(word, file_list_words)}
    return {selected_word: dict_tmp}


def get_random_word(list_words):
    random_word = list_words[random.randint(0, len(list_words))]
    return random_word
