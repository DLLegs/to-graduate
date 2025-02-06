# 백준 4134번 문제

import sys
input = sys.stdin.read
data = list(map(int, input().split()))
n = data[0]
test_case = data[1:]

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 ==0:
        return False
    i = 5
    # 약수의 성질을 이용
    while i*i <= num:
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True


for x in test_case:
    while not is_prime(x):
        x += 1
    print(x)

# 백준 13909 복습

n = int(input())
count = 0
for i in range(1, n+1):
    if i**2 < n:
        count += 1
    else:
        break
print(count)