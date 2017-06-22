import random
class subject:
    def __init__(self,id,name,len):
        self.id=id or random.randrange(1,10000)
        self.name=name or 'Random Name '+str(self.id)
        self.len=len or 0