import json,sys
from sub import subject
from user import person
from settings import *

def loadJSON(filePath='data_temp.json'):
    f = open(filePath, 'r', encoding="utf-8")
    lines = f.readlines()
    inp=''
    for x in lines:
        inp+=x
    inp=json.loads(inp)
    subjects={}
    people=[]
    for sub in inp['subjects']:
        tc=[]
        tc2=[]
        tc=inp['subjects'][sub].get('timeConstraints') or [(0,classesPerDay*5-1)]
        for se in tc:
            myse=se
            for day in range(1,5):
                if(myse[0]<classesPerDay*day and myse[1]>=classesPerDay*day):
                    tc2.append((myse[0],classesPerDay*day-1))
                    myse=(classesPerDay*day,myse[1])
                if(myse[0]>=myse[1]):
                    break
            tc2.append((myse[0],myse[1]))
        tcClean=[]
        for time in tc2:
            if((time[1]-time[0]+1)>=inp['subjects'][sub]['len']):
                tcClean.append(time)
        if(len(tcClean)==0):
            raise ValueError('A timeConstraints for a subject has no valid time periods.')
        subjects[sub]=subject(id=sub,name=inp['subjects'][sub]['name'],len=inp['subjects'][sub]['len'],timeConstraints=tcClean) 
    for cl in inp['people']:
        cl.sort()
        people.append(person(classes=cl))
    return subjects,people
    
loadJSON()