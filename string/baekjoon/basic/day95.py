# # 백준 11050번

# def fac(N, K):
#     if K == 0 or K == N:
#         return 1
#     return fac(N-1, K) + fac(N-1, K-1)

# N, K = map(int, input().split())
# print(fac(N, K))

## 백준 1463번

N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])