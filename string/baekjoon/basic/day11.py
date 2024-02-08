# 모듈
# 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일

import mod.mod1
print(mod.mod1.add(3,4))
print(mod.mod1.sub(9,4))

# from 모듈 이름 import 모듈 함수
from mod.mod1 import add
print(add(1, 2))

# 다수의 함수 사용시
# from 모듈 이름 import 함수1, 함수2
# from 모듈 이름 import *

import mod.mod2
print(mod.mod2.PI)

a = mod.mod2.Math()
print(a.solv(2))

print(mod.mod2.Math.add(mod.mod2.PI, 4.4))