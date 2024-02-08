# 백준 2738번 문제
# 입력값: N * M 크기 행렬
# 출력값: 두 행렬을 더한 값
n,m=map(int,input().split())
a=[[0 for col in range(m)] for row in range(n)] #이중 리스트 컴프리헨션
b=[[0 for col in range(m)] for row in range(n)]

for i in range(n):
    a[i]=list(map(int, input().split()))
for i in range(n):
    b[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j],end=" ")
    print()

# 백준 2566번 문제
# 입력값: 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉개의 수
# 출력값: 최대값과 행렬에서 그 위치, 두 개면 아무거나

import sys
input = sys.stdin.readline # 표준입력에서 한줄씩 빠르게 읽을 수 있음
table = []
for _ in range(9):
    table.append(list(map(int, input().split())))

X = 0
Y = 0
MAX = -1

for i in range(9):
    for j in range(9):
        if table[i][j] > MAX:
            MAX = table[i][j]
            X = i + 1
            Y = j + 1
print(MAX)
print(X, Y)
