import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

poe = open('Tell_Tale_Heart.txt','r',encoding = 'UTF-8')
telltale = poe.read().upper()
poe.close()
stopwords = set(STOPWORDS)
stopwords.add('UPON')
wc = WordCloud(margin=10,random_state=1, stopwords=stopwords, colormap='winter').generate(telltale)
wc.to_file('test.png')
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()
print(telltale)
#Documentation you may wish to consult
#https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html
#https://matplotlib.org/users/colormaps.html
