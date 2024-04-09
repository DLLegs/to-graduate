# 백준 9095번 문제
# 알고리즘 분류: 다이나믹 프로그래밍
# 메모이제이션 - 중복되는 계산을 피하기 위해 계산된 값을 저장해두고 필요할 때 마다 재활용
 

def count_ways(n):
    if n == 1:
        return 1
    if n == 2 :
        return 2
    if n == 3:
        return 4
# 다이나믹 프로그래밍을 위한 리스트 초기화
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    # 최적 부분 구조, 중복되는 부분 문제
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(count_ways(n))