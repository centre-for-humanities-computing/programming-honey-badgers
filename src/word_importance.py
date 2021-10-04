"""
https://towardsdatascience.com/how-important-are-the-words-in-your-text-data-tf-idf-answers-6fdc733bb066
"""

import pprint
import operator
from math import log10

# ingest data #
data = {
    'doc1':'TPol is smarter than the others',
    'doc2':'Janeway loves to explore the stars at night',
    'doc3':'The sun is shining in the sky',
    'doc4':'The night sky is full of start'
    }

# Preprocessing #

## lower case and tokenize
data_clean = []
for doc in data.values():
    doc_clean = doc.lower()
    doc_tokens = doc_clean.split(' ')
    data_clean.append(doc_tokens)

## flatten collection ##
all_data = []
for doc in data_clean:
    for token in doc:
        all_data.append(token)

## word counter

counter = {}
for token in all_data:
    counter.setdefault(token, 0)
    counter[token] = counter[token] + 1

pprint.pprint(counter) 

counter_sort = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

pprint.pprint(counter_sort) 

def word_count(text):
    """ count words in tokenized text
    """
    counter = {}
    for word in text:
        counter.setdefault(word, 0)
        counter[word] = counter[word] + 1
    
    return counter



# make word cloud here

##

lexicon = sorted(list(counter.keys()))
#print(lexicon)

# tdm  

tdm = []
for (doc, content) in data.items():
    null_doc = [0 for word in lexicon]
    wc = word_count(content.lower().split())
    #print(wc)
    for (i, word) in enumerate(lexicon):
        if word in wc:
            null_doc[i] = wc[word]
    #print(lexicon)
    #print(null_doc)
    tdm.append(null_doc)

# term frequency
tf_tdm = []
for doc in tdm:
    n = sum(doc)
    tf = [freq/n for freq in doc]
    tf_tdm.append(tf)


# inverse document frequency
idf = []
numerator = len(tdm)
for i in range(len(lexicon)):
    denominator = 0
    for j in range(len(tdm)):
        denominator = denominator + tdm[j][i]
    idf.append(log10(numerator/denominator))

#print(lexicon)
#print(df)


# TF-IDF
tfidf = []
for doc in tf_tdm:
    tfidf_doc = []
    for i in range(len(doc)):
        tfidf_doc.append(doc[i] * idf[i])
    tfidf.append(tfidf_doc)
    
    
# data summary

counter_tfidf = {}
for i in range(len(lexicon)):
    val = 0
    for j in (range(len(tfidf))):
        val = val + tfidf[j][i]
    counter_tfidf[lexicon[i]] = val

counter_tfidf_sort = sorted(counter_tfidf.items(), key=operator.itemgetter(1), reverse=True)


pprint.pprint(counter_tfidf_sort)

"""
for (i, doc) in enumerate(tdm):
    print(list(data.values())[i])
    print(lexicon)
    #print(doc)
    #print(tf_tdm[i])
    print(tfidf[i])
"""
    
#for word in lexicon:
