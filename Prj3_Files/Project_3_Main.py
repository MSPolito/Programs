from Project_3 import *
import nltk
import string

tweets = extract_tweets('sen_tweet1_edited_2.csv', 'state')
print(compare_hashes(tweets, level = 2))

tweets = extract_tweets('sen_tweet1_edited_2.csv', 'party')
print(compare_hashes(tweets, level = 15))
