import nltk #this will not work if you haven't installed nltk


def extract_tweets(filename, how = 'user'):
    #get the tweets out of the file and put them in a dictionary based on
    #a characteristic
    mappings = {'user':4, 'party':5, 'state':6}
    result = {}
    with open(filename,'r') as file:
        for line in file:
            data = line.split()
            tweet = process_tweet(data[2])
            if data[how] in result:
                result[data[how]] = tweet           
            else:
                result[data[how]].append(tweet)
            return result
    
def process_tweet(tweet):
    pass      


def compare_hashes(tweets, level = 10):
    pass   
    