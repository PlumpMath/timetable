import json,sys
from sub import subject
from user import person

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
        print(inp['subjects'][sub]['name'])
        subjects[sub]=subject(id=sub,name=inp['subjects'][sub]['name'],len=inp['subjects'][sub]['len']) 
    for cl in inp['people']:
        cl.sort()
        people.append(person(classes=cl))
    return subjects,people
    
loadJSON()