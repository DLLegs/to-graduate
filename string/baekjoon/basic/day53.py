# 백준 1978번 문제

n = int(input())
num = list(map(int, input().split()))
result = 0

for i in num:
    if i < 2:
        continue
    
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if(i % j == 0):
            is_prime = False
            break
    if is_prime:
        result += 1

print(result)