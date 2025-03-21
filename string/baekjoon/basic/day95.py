# 백준 11050번

def fac(N, K):
    if K == 0 or K == N:
        return 1
    return fac(N-1, K) + fac(N-1, K-1)

N, K = map(int, input().split())
print(fac(N, K))