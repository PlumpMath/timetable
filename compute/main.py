import numpy,re,random,os,json
import gene,user,genetools,jsonEncoder
import data_io as dio
from user import person
from sub import subject

generations=100
genes=10 #짝수로 맞추기

def main():
    runID="%8x"%random.getrandbits(32)
    print('Run ID '+runID)
    if not os.path.exists('result/'+runID):
        os.makedirs('result/'+runID)
    subjects,people=dio.loadJSON()
    genelist=genetools.randomGenes(genes,subjects)
    matchDict=user.subjectMatchDict(people,subjects)
    scoreValues={"best":[],"worst":[]}

    for i in range(0,generations):
        print('Generation '+str(i+1))
        genelist,best,worst=genetools.generation(genelist,subjects,matchDict)
        scoreValues['best'].append(best)
        scoreValues['worst'].append(worst)
        with open('result/'+runID+'/run_'+str(i+1)+'.json', 'w') as outfile:
            json.dump(genelist, outfile, indent=4, sort_keys=True)
    with open('result/'+runID+'/scores.json', 'w') as outfile:
        json.dump(scoreValues, outfile, indent=4, sort_keys=True)

if __name__=='__main__':
    main()