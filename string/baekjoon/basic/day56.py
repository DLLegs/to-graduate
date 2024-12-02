# # 백준 25305번 문제

# N, k = map(int, input().split())
# socre = list(map(int, input().split()))

# socre.sort(reverse=True)
# print(socre[k-1])

# 백준 2581번 문제

M = int(input())
N = int(input())
result = []

for i in range(M, N+1):
    e=0
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                e += 1
                break
        if e == 0:
            result.append(i)

if(len(result)>0):
    print(sum(result))
    print(min(result))
else:
    print(-1)