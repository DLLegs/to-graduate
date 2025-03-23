# 백준 2839번
# Greedy

N = int(input())
count = 0

while N >= 0:

    if N % 5 == 0:
        count += N // 5
        print(count)
        break
    N -= 3
    count += 1
else:
    print(-1)


# DP

n = int(input())
dp = [10000] * (n + 1)
dp[0] = 0

for i in range(1, n+1):
    if i >= 3:
        dp[i] = min(dp[i], dp[i-3] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5] + 1)

if dp[n] != 10000:
    print(dp[n])
else:
    print(-1)