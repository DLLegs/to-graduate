# 백준 2869번
# input = A: 올라가는 높이 B: 하강 V: 등반 목표
# output = 며칠을 걸려서 올라가는 지

A, B ,V = map(int,(input().split()))

day = (V - A) / (A - B) + 1
print(int(day) if day == int(day) else int(day)+1)