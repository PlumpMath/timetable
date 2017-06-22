import random
from sub import subject 

class person:
    def __init__(self,name='',classes=[]):
        self.name=name or 'Student '+str(random.randrange(100000,999999))
        if type(classes) is list:
            self.classes=classes

def subjectMatchDict(people,subjects):
    matchDict={}
    for id in subjects.keys():
        matchDict[id]={}
    for pl in people:
        pls=len(pl.classes)
        for i1 in range(0,pls-1):
            for i2 in range(i1+1,pls-1):
                a1=pl.classes[i1]
                a2=pl.classes[i2]
                if(a2 in matchDict[a1]):
                    matchDict[a1][a2]=matchDict[a1][a2]+1
                else:
                    matchDict[a1][a2]=1
    return matchDict