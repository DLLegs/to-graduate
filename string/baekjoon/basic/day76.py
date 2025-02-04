# 백준 1735번 문제

import math
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

num = A1*B2 + A2*B1
denom = B1 * B2
gcd = math.gcd(denom, num)

if gcd <= num:
    num = num//gcd # 소숫점이 나오지 않게 //로 나눔
    denom = denom//gcd

print(num, denom)

# 백준 11478번 복습

S = input().rstrip()
substring = set()

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        substring.add(S[i:j])

print(len(substring))