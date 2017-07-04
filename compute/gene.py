import random as rand
import json
from sub import subject
from settings import *

class gene:
    def __init__(self,pairs):
        self.genePairs={}
        for pair in pairs:
            self.genePairs[pair[0]]=(pair[1][0],pair[1][1])
        self.geneScore=(1<<62)
