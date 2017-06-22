import numpy,re
import gene,user,genetools
import data_io as dio
from user import person
from sub import subject

generations=100
genes=10 #짝수로 맞추기

def main():
    subjects,people=dio.loadJSON()
    genelist=genetools.randomGenes(genes,subjects)
    matchDict=user.subjectMatchDict(people,subjects)
    for i in range(0,generations):
        print('Generation '+str(i))
        genelist=genetools.generation(genelist,subjects,matchDict)

if __name__=='__main__':
    main()