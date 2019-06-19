import nltk #this will not work if you haven't installed nltk

def extract_tweets(tweetfile, how = 'user'):
    #get the tweets out of the file and put them in a dictionary based on
    #a characteristic
    result = {}
    data = {'user':-3,'state':-1,'party':-2}
    with open(tweetfile,'r', encoding="utf8") as file:
        for line in file:
            tweet = process_tweet(line).split()
            if tweet[data[how]] in result:
                result[tweet[data[how]]].append(tweet)
            else:
                result[tweet[data[how]]] = [tweet]
        return result
#above code is unfinished
def process_tweet(tweet):
    tweet = tweet.lower()
    specialCh = ',!?.+-$%^Z&*()_|'
    tweet.replace('&amp;', 'and')
    for i in specialCh:
        tweet.replace(i,"")
    return tweet
def compare_hashes(tweetdict, level = 10):
    hashtags = {}
    currentcont = 0
    for catagory in tweetdict:
            hashes = []
            for tweet in tweetdict[catagory]:
                for word in tweet:
                    if word[0] == "#":
                        hashes.append(word)
            if hashes != []:
                hashes.sort()
                lasthash = hashes[0]
                hashcount = 0
                tempCatagoryHashes = []
                for hash in hashes:
                    if hash == lasthash:
                        hashcount +=1
                    else:
                        tempCatagoryHashes.append([hashcount, hash])
                        hashcount = 1
                    lasthash = hash
                tempCatagoryHashes.sort(reverse = True)
                catagoryHashes = []
                itemcount = 0
                for item in tempCatagoryHashes:
                    if itemcount < level:
                        catagoryHashes.append(tempCatagoryHashes[itemcount])
                        itemcount += 1
                itemcountreverse = 0
                for item in catagoryHashes:
                    catagoryHashes[itemcountreverse] = (item[1],item[0])
                    itemcountreverse +=1
                hashtags[catagory] = catagoryHashes
    return hashtags
'''
Take in the tweets
find hashtags
pair with state
return dict of hashtag counts per how variable

'''
#     pass
