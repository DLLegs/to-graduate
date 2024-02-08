# 백준 12865번 문제
# 동적 프로그래밍, 냅색알고리즘

N, K = map(int, input().split())
items = []

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

# 동적 프로그래밍
dp = [[0] * (K + 1) for _ in range(N + 1)]

# i는 가치를 찾기위한 인덱스 역할, j는 식별하기 위한 무게
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight, value = items[i - 1]

        # 현재 물건을 배낭에 넣을 수 있는 경우와 넣지 않는 경우 중 큰 가치 선택
        # 이 부분이 이해가 안됨
        if j >= weight:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])
