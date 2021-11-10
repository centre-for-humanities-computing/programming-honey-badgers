from scipy import spatial

def tokenizer(text):
    return text.split()

def word_count(text, sort = True):
    """ count words
    """
    counter = {}
    for word in tokenizer(text):
        counter.setdefault(word, 0)
        counter[word] = counter[word] + 1
    
    return counter

def list_to_dtm(corpus):
    """ build document term matrix from list of string documents
    """
    wc = word_count(' '.join(corpus))
    lexicon = sorted(list(wc.keys()))
    
    dtm = []
    for content in corpus:
        document = [0 for _ in lexicon]
        wc = word_count(content)
        for (i, word) in enumerate(lexicon):
            if word in wc:
                document[i] = wc[word]
        
        dtm.append(document)
    
    return dtm, lexicon

texts = [
    "cyberspace a consensual hallucination experienced daily by billions of legitimate operators in every nation",
    "the internet is becoming the town square for the global village of tomorrow",
    "cyberspace is the funhouse mirror of our own society",
]
dtm, lexicon = list_to_dtm(texts)

print('[INFO] Cosine similarity for pairwise document comparison')
print('[INFO] Document 1 and 2:')
print(1 - spatial.distance.cosine(dtm[0],dtm[1]))
print('[INFO] Document 1 and 3:')
print(1 - spatial.distance.cosine(dtm[0],dtm[2]))
print('[INFO] Document 2 and 3:')
print(1 - spatial.distance.cosine(dtm[1],dtm[2]))
