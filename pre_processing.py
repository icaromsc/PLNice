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
    file = open("/home/infobio/PycharmProjects/PLNice/english_stop_words.txt", "r")
    words=file.read().split()
    return words


def removeStopWords(file,stopwords):
    removed=[]
    file = removeJunk(file)
    file=file.split()
    for f in file:
        if f.lower() not in stopwords:
            removed.append(f)
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
    processeds.append(processeds)




print "*\n*\ntexts processed",len(processeds)
print "*\n*\nn terms:",len(terms)
print "terms:\n*\n",terms
print "freq terms:\n*\n",freqTerms[0]









