#test functionality of parser

from nose.tools import *
from parser import *
from ex49 import lexicon

class TestSentence(object):
    def make_wordlist(sentence):
        return scan(sentence)

testsentence = TestSentence.make_wordlist("Run north and kill the bear")

def test_peek():
    parser.peek.word_list = testsentence
    print(parser.peek(word_list))

def test_match():
    pass

def test_skip():
    pass

def test_parse_verb():
    pass

def test_parse_object():
    pass

def test_parse_subject():
    pass

def test_parse_sentence():
    pass
