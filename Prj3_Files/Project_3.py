import nltk #this will not work if you haven't installed nltk

def extract_tweets('test_file.txt', 'r', how = 'user'):
    #get the tweets out of the file and put them in a dictionary based on
    #a characteristic
    result = []
    with open('test_file.txt','r') as file:
        for line in file:
            data = line.split()
            tweet = process_tweet(data[2])
            if data[how] in result:
                result[data[how]] = tweet
            else:
                result[data[how]].append(tweet)
            return result
#above code is unfinished
def process_tweet(tweet):
  tw = itw.lower().translate('%amp', '    ').maketrans('', '', ',!?.+-$%^Z&*()_|')
  return tw
print(tw)
    # pass

def compare_hashes(tweets, level = 10):
  hashtags = []
  for word in test_file:
    state =  testfile[-2:]
    srtlst = state.sort()
    hstg = srtlst.find('#')

print(new_text)
#     pass
