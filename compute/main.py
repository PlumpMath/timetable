import numpy,re,random,os,json,codecs,operator
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

    with codecs.open('result/'+runID+'/input.json', 'w', encoding="utf-8") as outfile:
        json.dump({"subjects":subjects, "people":people}, outfile, indent=4, sort_keys=True, ensure_ascii=False)
    
    for i in range(0,generations):
        print('Generation '+str(i+1))
        genelist=genetools.generation(genelist,subjects,matchDict)
        genelist.sort(key=operator.attrgetter('geneScore'))
        best=genelist[0].geneScore
        worst=genelist[-1].geneScore
        print('Best Score: '+str(best)+', Worst Score: '+str(worst))
        scoreValues['best'].append(best)
        scoreValues['worst'].append(worst)
        with codecs.open('result/'+runID+'/run_'+str(i+1)+'.json', 'w', encoding="utf-8") as outfile:
            json.dump(genelist, outfile, indent=4, sort_keys=True, ensure_ascii=False)
    
    with codecs.open('result/'+runID+'/scores.json', 'w', encoding="utf-8") as outfile:
        json.dump(scoreValues, outfile, indent=4, sort_keys=True, ensure_ascii=False)

    with codecs.open('result/'+runID+'/info.json', 'w', encoding="utf-8") as outfile:
        outfile.write('{ \"runCount\": '+str(generations)+' }')

if __name__=='__main__':
    main()