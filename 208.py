class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self,first,second):
            self.first=first
            self.second=second    
        
    def add(self):
        result= self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first * self.second
        return result
    def div(self):
        result=self.first /self.second
        return result
a=FourCal(2,4)

class MoreFourCal(FourCal):
    pass
    