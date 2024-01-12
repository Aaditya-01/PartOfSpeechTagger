import pytest

from .structures import Document, sentencize, tokenize

def test_Document_Token_Sentence():
    document = Document('A paragraph is a series of related sentences developing a central idea, called the topic. ')
    assert document.raw == ('A paragraph is a series of related sentences developing a central idea, called the topic. ')
    assert document.sentences[0] == 'A paragraph is a series of related sentences developing a central idea, called the topic. '
    assert document[0] == 'A paragraph is a series of related sentences developing a central idea, called the topic. '
    assert len(document.sentences) == 1
    document = Document('A paragraph is a series of related sentences developing a central idea, called the topic. Paragraphs add one idea at a time to your broader argument.')
    assert len(document.sentences) == 2
    assert document.sentences[0] == 'A paragraph is a series of related sentences developing a central idea, called the topic. '
    assert len(document.sentences[0].tokens) == 15
    assert document.sentences[1] == 'Paragraphs add one idea at a time to your broader argument.'
    assert document.sentences[0].next_sentence == document.sentences[1]
    assert document.sentences[1].previous_sentence == document.sentences[0]
    assert document.sentences[0].tokens[0] == '<SOS>'
    assert document[0][0] == '<SOS>'
    assert document.sentences[0].tokens[1] == 'All'
    assert document.sentences[0].tokens[-2] == '.'
    document = Document('The number of pi is usually summarized to 3.14 for the sake of simplicity. The greek letter pi was adopted by William Jones in 1706. Nice, right?')
    assert len(document.sentences) == 3
    assert document.sentences[2] == "Nice, right?"
    assert len(document.sentences[0].tokens) == 17

def test_sentencize():
    text = 'A paragraph is a series of related sentences developing a central idea, called the topic. Paragraphs add one idea at a time to your broader argument...'
    assert len(sentencize(text)) == 2
    text = 'The number of pi is usually summarized to 3.14 for the sake of simplicity. The greek letter pi was adopted by William Jones in 1706. Nice, right? All human beings are born free and equal in dignity and rights. .15 ... okay. All human beings are born free and equal in dignity and rights. ok . a'
    assert len(sentencize(text)) == 9

def test_tokenize():
    sentence = 'The number of pi is usually summarized to 3.14 for the sake of simplicity.'
    tokens = tokenize(sentence)
    assert len(tokens) == 17
    assert tokens[-2].next_token.EOS==True
    assert tokens[1].previous_token.SOS==True
    assert tokens[3].next_token==tokens[4]
    assert tokens[4].previous_token == tokens[3]
    assert tokens[-2]=='.'
