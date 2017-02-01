#test functionality of parser

from nose.tools import *
from ex49 import parser
from ex49.lexicon import scan

class TestSentence(object):
    def make_wordlist(sentence):
        return scan(sentence)

testsentence = TestSentence.make_wordlist("Run north and kill the bear")


def test_peek():
    assert_equal(parser.peek(testsentence), testsentence[0])

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
