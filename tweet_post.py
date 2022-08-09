import spacy
import re
import markovify
import tweepy
import random
import datetime

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Creates the post and logs to a file
def generate_post():
    with open('jorpson.txt') as f:
        text = f.read()
    with open('jorpson2.txt') as f:
        text = f.read()
    with open('jorpson3.txt') as f:
        text = f.read()
    with open('jorpson4.txt') as f:
        text = f.read()
        
    nlp = spacy.load("en_core_web_sm")
        
    text1_doc=nlp(text1)
    text2_doc=nlp(text2)
    text3_doc=nlp(text3)
    text4_doc=nlp(text4)

    text1_sents = ' '.join([sent.text for sent in text1_doc.sents if len(sent.text) > 1])
    text2_sents = ' '.join([sent.text for sent in text2_doc.sents if len(sent.text) > 1])
    text3_sents = ' '.join([sent.text for sent in text3_doc.sents if len(sent.text) > 1])
    text4_sents = ' '.join([sent.text for sent in text4_doc.sents if len(sent.text) > 1])
    corp = text1_sents + text2_sents + text3_sents + text4_sents

    generator_1 = markovify.Text(corp, state_size=3)

    sent1=generator_1.make_sentence(min_chars=300)
    sent2=generator_1.make_sentence(min_chars=300)
    sent3=generator_1.make_sentence(min_chars=300)
    sent4=generator_1.make_sentence(min_chars=300)
    
    if len(sent1)>300:
        print(sent1)
    elif len(sent2)>300:
        print(sent2)
    elif len(sent3)>300:
        print(sent3)
    else:
        print(sent4)

        
#generate_post()

# Post the status to Twitter
    api.update_status(status=generate_post())
