import pytest
from vowels import count_vowels

def test_only_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_no_vowels():
    assert count_vowels("") == 0
    assert count_vowels("bcdfg") == 0
    assert count_vowels("12345") == 0

def test_mixed_strings():
    assert count_vowels("hello") == 2
    assert count_vowels("HeLLo WoRLd") == 3
    assert count_vowels("PyThOn PrOgRaMmInG") == 5
