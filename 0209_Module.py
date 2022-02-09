# 모듈 - 함수나 변수 또는 클래스를 모아 놓은 파일

# 모듈 호출
import mod1

print(mod1.add(1,2))

print(mod1.sub(2,1))

# 모듈 안 함수만 호출
from mod1 import add

print(mod1.PI)

a= mod1.Math()
print(a.solv(3))

# Math는 안되고 Math()는 되는 이유 : 단일 단어 Math는 그 자체를 불러오고 뒤에 () 가 붙으면
# Math 안에 포함된 모든 걸 불러온다고 생각하자
print(add(mod1.Math().solv(3),2))