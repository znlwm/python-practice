# 클래스 사칙연산
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

# 상속
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first ** self.second
        return result
                

# 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first / self.second

a=SafeFourCal(4,0)
print(a.div())

# 클래스 변수
class Family:
    lastname="최"
    
# print(Family.lastname)
a=Family
print(a.lastname)