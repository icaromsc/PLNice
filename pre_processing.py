from os import getcwd

mypath=(getcwd())
def getListFiles(mypath):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #print onlyfiles
    return onlyfiles

def openFiles(listFiles):
    texts=[]
    for i in listFiles:
        file=open(mypath + "/" + i, "r")
        texts.append(file.read())
    return texts

print mypath
texts=openFiles(getListFiles(mypath))
print texts[0]


