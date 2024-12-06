# File: tests/test_vowel_remover.py

from lib.Debugging import *

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

def test_multiple_vowels_in_a_row():
    remover = VowelRemover("Books and Nooks")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "Bks nd Nks"

def test_only_vowels():
    remover = VowelRemover("aeiou")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""