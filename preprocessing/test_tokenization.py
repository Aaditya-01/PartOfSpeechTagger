import pytest

from .tokenization import DummySentencizer, DummyTokenizer

def test_dummysentencizer():
    sentences = DummySentencizer('A paragraph is a series of related sentences developing a central idea, called the topic. Paragraphs add one idea at a time to your broader argument.')
    assert sentences.sentences == ['A paragraph is a series of related sentences developing a central idea, called the topic.','Paragraphs add one idea at a time to your broader argument.']
    sentences = DummySentencizer('')
    assert sentences.sentences == []
    sentences = DummySentencizer(4)
    assert sentences.sentences == ['4']
    sentences = DummySentencizer('...')
    assert sentences.sentences == ['.','.','.']

def test_dummytokenizer():
    tokens = DummyTokenizer('A paragraph is a series of related sentences developing a central idea, called the topic.')
    assert tokens.tokens == ['A','paragraph','is','a','series','of','related','sentences','developing','a','central','idea',',','called','the','topic','.']
