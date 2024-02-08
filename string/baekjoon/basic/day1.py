a='life is too short, you need python'
print(a[0:4]) # [이상:미만:간격] 슬라이싱

a='20230627Rainy'
print(a[0:8])

a='123456789'
print(a[::2])

# 문자열 포멧팅 (따움표를 계속 열고 안 닫아도 됨)
number=10
day='two'
a='I ate %d apples. so I was sick %s days'%(number, day)
print(a)

b='hi my name is {name} and I\'m {postion}'.format(name='vardy', postion='ST')
print(b)

# 소숫점 자리 남기기
a="%0.4f" %3.141592
print(a)

