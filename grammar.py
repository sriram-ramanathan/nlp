import nltk

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document) 
    sentences = [nltk.word_tokenize(sent) for sent in sentences] 
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

docs=ie_preprocess(samp)

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), 
... ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

grammar = "Authors: {(<Byline>*<NNP><,>*<NNP>*)*}" 

cp = nltk.RegexpParser(grammar) 
result = cp.parse(docs[0]) 
print(result) 
