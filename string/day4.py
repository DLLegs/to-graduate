# bool 자료형

a = True
b = False

print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>

print(2>1) # True

# 변수
# 변수_이름 = 변수에_저장할_값

a = [1, 2, 3]
print(id(a)) # 변수가 가지고 있는 객체의 주소 값

b = a # 리스트 복사됨
print(id(b)) # 동일한 객체를 가리키고 있기 때문에 같은 주소 값

# 다른 주소를 가리키게 만드며 복사하는 방법

# [:] 이용하기
c = [1, 2, 3]
d = c[:]
c[1] = 4
print(c) # [1, 4, 3]
print(d) # [1, 2, 3]

# copy 모듈 이용하기
from copy import copy
e = [1, 2, 3]
f = copy(e)
print(e is f) # False 서로 다른 값임을 알려준다
