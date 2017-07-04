import random as rand
import json
from settings import *

class subject:
    def __init__(self,id,len,room,name=None,timeConstraints=None):
        self.id=id or rand.randrange(1,10000)
        self.name=name or 'Random Name '+str(self.id)
        self.room=room
        self.len=len or 0
        self.timeConstraints=timeConstraints or None #(s,e) tuple list

class room:
    def __init__(self,id,name=None):
        self.id=id
        self.name=name or '교실 #'+str(rand.randrange(100000,999999))

class gene:
    def __init__(self,pairs):
        self.genePairs={}
        for pair in pairs:
            self.genePairs[pair[0]]=(pair[1][0],pair[1][1])
        self.geneScore=(1<<62)

class person:
    def __init__(self,name='',classes=[]):
        self.name=name or '학생 #'+str(rand.randrange(100000,999999))
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