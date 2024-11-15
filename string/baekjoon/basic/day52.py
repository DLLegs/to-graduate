# 백준 2869번
# input = A: 올라가는 높이 B: 하강 V: 등반 목표
# output = 며칠을 걸려서 올라가는 지

# 정상에 도착하면 더이상 내려가지 않음
# V = day * (A - B) + A
# 여기서 마지막 A는 마지막날 정상에 도착을 의미
# day = (V - A)/(A - B) + 1
# + 1 은 마지막 날이 빠졌기 때문
# 삼항 연산자
# [True] if [조건문(Condition)] else [False]

A, B ,V = map(int,(input().split()))

day = (V - A) / (A - B) + 1
print(int(day) if day == int(day) else int(day)+1)