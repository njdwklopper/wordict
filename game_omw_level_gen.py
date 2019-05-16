# Create Anagram Game boards

from word_utils import *

tmp_word = get_random_word(get_list_words_by_length(MAXIMUM_WORD_LENGTH))
print("Chosen word: " + tmp_word)

tmp_list_words_for_board = get_list_words_by_word(tmp_word)
print(tmp_list_words_for_board)

# TODO: create anagram game board json files
