# Create Anagram Game boards

from word_utils import *

file_list_words = open("dictionary/word_data.json", "r").read()
tmp_word = get_random_word(get_list_words_by_length(MAXIMUM_WORD_LENGTH, file_list_words))
print("Chosen word: " + tmp_word)

tmp_list_words_for_board = get_list_words_by_word(tmp_word, file_list_words)
print(tmp_list_words_for_board)

print("List length: " + str(len(file_list_words)))
tmp_game_level = get_game_level(0, file_list_words)
print(tmp_game_level)
tmp_game_level = get_game_level(11924, file_list_words)
print(tmp_game_level)
# TODO: create anagram game board json files
