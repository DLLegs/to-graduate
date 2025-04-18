# 백준 1978번 (약수, 배수, 소수)

N = int(input())
num = map(int, input().split())
count = 0
for i in num:
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += 1

print(count)