# 백준 2530번 문제
# 예제 입력 17 40 45 enter 6015
# 출력 19 21 0

H, M, S = map(int, input().split())
Plus = int(input())

total_seconds = H * 3600 + M * 60 + S + Plus

H = total_seconds // 3600
M = (total_seconds % 3600) // 60
S = total_seconds % 60

if H >= 24:
    H %= 24

print(H, M, S)
