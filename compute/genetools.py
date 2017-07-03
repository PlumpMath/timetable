import random as rand
from sub import subject
from gene import gene
from user import person
import operator,copy

classesPerDay = 12
mutationRate = 0.05

def randomPairs(subjects):
    ret=[]
    for subkey in subjects.keys():
        subject = subjects[subkey]
        randDay=rand.randrange(0,5)
        randTime=rand.randrange(0,classesPerDay+1-subject.len) #9교시까지
        startTime=randDay*classesPerDay+randTime
        endTime=randDay*classesPerDay+randTime+subject.len-1
        ret.append((subject.id,(startTime,endTime)))
    return ret

def randomGenes(geneCount,subjects):
    retu=[]
    for i in range(0,geneCount):
        retu.append(gene(randomPairs(subjects)))
    return retu
    
def evalGene(gene,subjects,matchDict):
    ret=0
    priceDict={}
    for s1 in subjects.keys():
        priceDict[s1]={}
        for s2 in subjects.keys():
            if(s1>=s2):
                continue
            ts1=gene.genePairs[s1]
            ts2=gene.genePairs[s2]
            if(ts1[1]<ts2[0] or ts2[1]<ts1[0]):
                priceDict[s1][s2]=0
            else:
                l1=subjects[s1].len
                l2=subjects[s2].len
                priceDict[s1][s2]=(l1+l2)-(max(ts1[1],ts2[1])-min(ts1[0],ts2[0])+1)
    for i1 in matchDict.keys():
        for i2 in matchDict[i1].keys():
            ret=ret+(matchDict[i1][i2]*priceDict[i1][i2])
    return ret

def evalGeneGroup(genes,subjects,matchDict):
    ret=[]
    print('Evaluating Gene Group')
    for gene in genes:
        score = evalGene(gene,subjects,matchDict)
        ret.append(score)
    return ret

def generation(genes,subjects,matchDict):
    scores = evalGeneGroup(genes,subjects,matchDict)
    for i in range(0,len(genes)):
        genes[i].geneScore=scores[i]
    genes.sort(key=operator.attrgetter('geneScore'))
    pairs=genes[0:int(len(genes)/2)]
    for i in range(0,int(len(genes)/4)):
        np1,np2=newPairs(genes[2*i],genes[2*i+1],subjects,matchDict)
        pairs.extend([np1,np2])
    if(len(pairs)%2==1):
        pairs.append(genes[0])
    return pairs
    
def newPairs(gene1,gene2,subjects,matchDict):
    mg1=copy.deepcopy(gene1)
    mg2=copy.deepcopy(gene2)
    mut1=randomPairs(subjects)
    mut2=randomPairs(subjects)
    ev1=(1<<62)
    ev2=(1<<62)
    #Mutation
    ind=0
    for gk in gene1.genePairs.keys():
        nmg1=copy.deepcopy(mg1)
        if(rand.random()<=mutationRate):
            mg1.genePairs[gk]=mut1[ind][1]
        else:
            nmg1.genePairs[gk]=gene2.genePairs[gk]
        nev1=evalGene(nmg1,subjects,matchDict)
        if(nev1<ev1):
            mg1=copy.deepcopy(nmg1)
            ev1=nev1
        ind=ind+1
    
    ind=0
    for gk in gene2.genePairs.keys():
        nmg2=copy.deepcopy(mg2)
        if(rand.random()<=mutationRate):
            mg2.genePairs[gk]=mut2[ind][1]
        else:
            nmg2.genePairs[gk]=gene1.genePairs[gk]
        nev2=evalGene(nmg2,subjects,matchDict)
        if(nev2<ev2):
            mg2=copy.deepcopy(nmg2)
            ev2=nev2
        ind=ind+1
    
    mg1.geneScore=ev1
    mg2.geneScore=ev2
    return mg1,mg2