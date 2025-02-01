# 백준 1269번 문제

import sys
input = sys.stdin.read

data = input().splitlines()  # 함수 호출 추가
n, m = map(int, data[0].split())

A = set(map(int, data[1].split()))
B = set(map(int, data[2].split()))  # 슬라이싱 범위 수정

union = A & B
print(n+m-2*len(union))

# 백준 1764번 복습

import sys
Input = sys.stdin.read
Data = Input().splitlines()
N, M = map(int, Data[0].split())
no_hear = set(Data[1:N+1])
no_see = set(Data[N+1:N+M+1])

no_hear_see = sorted(no_hear & no_see)
print(len(no_hear_see))
print('\n'.join(no_hear_see))