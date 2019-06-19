import nltk #this will not work if you haven't installed nltk

def extract_tweets(tweetfile, party, how = 'user'):
    #get the tweets out of the file and put them in a dictionary based on
    #a characteristic
    result = {}
    with open(tweetfile,'r') as file:
        for line in file:
            line = process_tweet(line)
            data = {'user': -3, 'party': -2, 'state': -1}
            if data[how] in result:
                result[data[how]].append(line)
            else:
                result[data[how]] = line
        return result
#above code is unfinished
def process_tweet(tweet):
    trantab = maketrans('&amp', 'and')
    tweet = tweet.lower().translate(trantab)
    specialch = ',!?.+-$%^Z&*()_|'
    for i in specialch:
        tweet.replace(i , '')
    return tweet
    # pass

def compare_hashes(tweets, level = 10):
  hashtags = []
  for word in test_file:
    state =  testfile[-1:]
    srtlst = state.sort()
    hstg = srtlst.find('#')
    cthstg = hstg.count()
    tweets = (cthstg, hstg)
    return(tweets)
#     pass
