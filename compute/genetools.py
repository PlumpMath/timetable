import random as rand
from sub import subject
from gene import gene
from user import person
import operator,copy

#최대 교시 수
classesPerDay = 12
#돌연변이 비율
mutationRate = 0.05

#randomGenes에서 사용하기 위한 유전자 쌍을 제작
def randomPairs(subjects):
    ret=[]
    #과목별로 유전자 쌍 생성: [i,j] 형태의 폐구간으로 이루어짐
    #i: 시작 시간, j: 끝 시간. 전부 (요일)*classesPerDay+(교시)로 이루어짐
    #교시는 0-indexed
    for subkey in subjects.keys():
        subject = subjects[subkey]
        #요일 무작위 선택. 월:0~금:4 이므로 [0,5)에서 무작위 선택
        randDay=rand.randrange(0,5)
        #시작하는 교시 선택. 끝나는 시간이 classPerDay미만이므로 [0,classesPerDay+1-(수업 길이))로 선택
        randTime=rand.randrange(0,classesPerDay+1-subject.len) #9교시까지
        #16번줄의 설명처럼 쌍 생성, 삽입.
        startTime=randDay*classesPerDay+randTime
        endTime=randDay*classesPerDay+randTime+subject.len-1
        #(수업 ID,(시작시간,끝시간)) 형식의 튜플
        ret.append((subject.id,(startTime,endTime)))
    return ret

#필요한 개수만큼 무작위 유전자 쌍을 생성한다. randomPairs를 돌려서 gene 객체를 만들어내는 역할
def randomGenes(geneCount,subjects):
    retu=[]
    for i in range(0,geneCount):
        retu.append(gene(randomPairs(subjects)))
    return retu
    
#유전자 점수 평가
#개선의 여지가 아주 많다...
def evalGene(gene,subjects,matchDict):
    ret=0
    priceDict={}
    #유전자에 포함된 수업들의 겹치는 경우들을 모두 찾음
    for s1 in subjects.keys():
        priceDict[s1]={}
        for s2 in subjects.keys():
            #s1<s2인 경우만 체크해 중복을 방지함
            if(s1>=s2):
                continue
            ts1=gene.genePairs[s1]
            ts2=gene.genePairs[s2]
            #겹치지 않을 경우
            if(ts1[1]<ts2[0] or ts2[1]<ts1[0]):
                priceDict[s1][s2]=0
            #겹칠 경우: (두 수업의 길이 합)-(두 수업이 만드는 구간 길이)로 몇 교시가 겹치는지 판정
            else:
                l1=subjects[s1].len
                l2=subjects[s2].len
                priceDict[s1][s2]=(l1+l2)-(max(ts1[1],ts2[1])-min(ts1[0],ts2[0])+1)
    #이전에 계산한 matchDict로 점수를 매김
    for i1 in matchDict.keys():
        for i2 in matchDict[i1].keys():
            ret=ret+(matchDict[i1][i2]*priceDict[i1][i2])
    return ret

#여러 유전자를 한꺼번에 평가. 그냥 for문 돌려주는 함수
def evalGeneGroup(genes,subjects,matchDict):
    ret=[]
    print('Evaluating Gene Group')
    for gene in genes:
        score = evalGene(gene,subjects,matchDict)
        ret.append(score)
    return ret

#한 세대를 진행. 유전자 평가, 교차를 통한 새로운 세대를 생성함
def generation(genes,subjects,matchDict):
    #유전자의 평가
    scores = evalGeneGroup(genes,subjects,matchDict)
    #점수를 구한 후 각 유전자의 geneScore 필드에 점수를 저장
    for i in range(0,len(genes)):
        genes[i].geneScore=scores[i]
    #점수로 오름차순 정렬
    genes.sort(key=operator.attrgetter('geneScore'))
    #상위 50%는 그대로 유지
    pairs=genes[0:int(len(genes)/2)]
    #상위 50%끼리 교차
    for i in range(0,int(len(genes)/4)):
        np1,np2=newPairs(genes[2*i],genes[2*i+1],subjects,matchDict)
        pairs.extend([np1,np2])
    #홀수개가 남을 경우 그냥 이전 세대에서 가장 좋았던 유전자를 다시 넣음
    if(len(pairs)%2==1):
        pairs.append(genes[0])
    return pairs
    
#두 유전자가 주어지면 새로운 쌍을 생성
def newPairs(gene1,gene2,subjects,matchDict):
    #교차 결과 유전자. copy.deepcopy는 검색ㄱㄱ
    mg1=copy.deepcopy(gene1)
    mg2=copy.deepcopy(gene2)
    #돌연변이가 일어날 경우 변하는 유전자쌍을 미리 저장해둠
    mut1=randomPairs(subjects)
    mut2=randomPairs(subjects)
    #교차한 유전자의 점수
    ev1=(1<<62)
    ev2=(1<<62)
    #Mutation
    ind=0
    #유전자 1을 베이스로 한 교차
    for gk in gene1.genePairs.keys():
        #비교 대상이 될 유전자를 복사해둠
        nmg1=copy.deepcopy(mg1)
        #돌연변이
        if(rand.random()<=mutationRate):
            mg1.genePairs[gk]=mut1[ind][1]
        #아니라면 유전자 2에서 유전자쌍을 갖고옴
        else:
            nmg1.genePairs[gk]=gene2.genePairs[gk]
        #유전자를 바꿨을때의 점수 계산
        nev1=evalGene(nmg1,subjects,matchDict)
        #바꿨을때 점수가 낮아진다면 새로운 유전자로 변경
        if(nev1<ev1):
            mg1=copy.deepcopy(nmg1)
            ev1=nev1
        ind=ind+1
    
    #유전자 2를 베이스로 한 교차
    #위 참조 (완전 똑같음)
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
    #가장 좋은 유전자 내에 점수 저장, 리턴
    mg1.geneScore=ev1
    mg2.geneScore=ev2
    return mg1,mg2