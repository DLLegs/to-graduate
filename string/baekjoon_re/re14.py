# 백준 2563번 (2차원 배열)

N = int(input())
papper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            papper[i][j] = 1

res = 0
for i in papper:
    res += sum(i)

print(res)