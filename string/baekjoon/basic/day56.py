# 백준 25305번 문제

N, k = map(int, input().split())
socre = list(map(int, input().split()))

socre.sort(reverse=True)
print(socre)
print(k)
print(socre[k-1])
