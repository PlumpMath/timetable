import json,sys
from sub import subject
from user import person

def loadJSON(filePath='data_temp.json'):
    f = open(filePath, 'r')
    lines = f.readlines()
    inp=''
    for x in lines:
        inp+=x
    inp=json.loads(inp)
    subjects={}
    people=[]
    for sub in inp['subjects']:
        subjects[sub['id']]=subject(id=sub['id'],name=sub['name'],len=sub['len']) 
    for cl in inp['people']:
        cl.sort()
        people.append(person(classes=cl))
    return subjects,people
    
loadJSON()