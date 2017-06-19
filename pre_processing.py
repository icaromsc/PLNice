from os import getcwd
from collections import Counter

mypath=(getcwd()+"/texts/")



def getListFiles(mypath):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #print onlyfiles
    return onlyfiles


def openFiles(listFiles):
    texts=[]
    for i in listFiles:
        file=open(mypath  + i, "r")
        texts.append(file.read())
    return texts


def getStopWords():
    file = open(getcwd()+"/english_stop_words.txt", "r")
    words=file.read().split()
    return words


def removeStopWords(file,stopwords):
    removed=[]
    file = removeJunk(file)
    file=file.split()
    for f in file:
        if f.lower() not in stopwords:
            removed.append(f.lower())
    return removed

def removeJunk(file):
    file = file.replace(":", "")
    file = file.replace(",", "")
    file = file.replace(".", "")
    file = file.replace("?", "")
    file = file.replace(")", "")
    file = file.replace("(", "")
    file = file.replace(";", "")
    return file


def createTF(terms,documents):
    tf = []
    for t in terms:
        documentFreq = []
        for d in documents:
            counter = d.count(t)
            documentFreq.append(counter)
        print t, ": ", documentFreq, 'ranq:', sum(documentFreq)
        temp=[]
        temp.append(t)
        temp.append(sum(documentFreq))
        tf.append(temp)
        # print 'termo ', 'align', ' no doc ', i, 'freq:', counter
    return tf


def myTF(terms,documents):
    tf = []
    for t in terms:
        documentFreq = []
        for d in documents:
            counter = d.count(t)
            documentFreq.append(counter)
        #print t, ": ", documentFreq, 'ranq:', sum(documentFreq)
        temp = []
        temp.append(t)
        temp.append(documentFreq)
        tf.append(temp)
        # print 'termo ', 'align', ' no doc ', i, 'freq:', counter
    return tf


def viewMatrix(lista):
    for l in lista:
        print l


#inicializacao
print mypath
texts=openFiles(getListFiles(mypath))
#print texts[0]
words=getStopWords()
print "stopwords:\n"
print words
processeds=[]
terms=set()
freqTerms=[]

#remove stopwords
for text in texts:
    print "texto:\n*\n*\n",text
    processed=removeStopWords(text,words)
    print "texto sem stopwords:\n*\n*\n",processed
    freqTerms.append(Counter(processed))
    terms.update(set(processed))
    print "n palavras txt original:", len(text)
    print "n palavras txt processado:", len(processed)
    processeds.append(processed)




print "*\n*\ntexts processed",len(processeds)
print "*\n*\nn terms:",len(terms)
print "terms:\n*\n",terms
print "freq terms:\n*\n",freqTerms[0]
#createTF(terms,processeds)
tf=myTF(terms,processeds)
ranq_tf = createTF(terms,processeds)
tf=sorted(tf, key=lambda x: x[1], reverse=True)
viewMatrix(tf)
v=sorted(ranq_tf, key=lambda x: x[1], reverse=True)
viewMatrix(v)
#from operator import itemgetter
#print sorted(.items(), key=itemgetter(1))










