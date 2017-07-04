import random
from settings import *
class subject:
    def __init__(self,id,len,name=None,timeConstraints=None):
        self.id=id or random.randrange(1,10000)
        self.name=name or 'Random Name '+str(self.id)
        self.len=len or 0
        self.timeConstraints=timeConstraints or None #(s,e) tuple list