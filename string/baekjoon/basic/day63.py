# # 백준 1018번 문제

N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 최소 칠해야 할 횟수를 저장할 변수
min_count = float('inf')

# 모든 8x8 체스판을 확인
for i in range(N - 7):
    for j in range(M - 7):
        draw1 = 0  # "W" 시작
        draw2 = 0  # "B" 시작
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:  # 짝수 칸
                    if board[a][b] != "W":
                        draw1 += 1
                    if board[a][b] != "B":
                        draw2 += 1
                else:  # 홀수 칸
                    if board[a][b] != "B":
                        draw1 += 1
                    if board[a][b] != "W":
                        draw2 += 1
        # 두 경우의 최소값을 비교하여 업데이트
        min_count = min(min_count, draw1, draw2)

print(min_count)



n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = float('inf')

for i in range(n-7):
    for j in range(m-7):
        w_index = 0
        b_index = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if board[a][b] != "W":
                        w_index += 1
                    if board[a][b] != "B":
                        b_index += 1
                else:
                    if board[a][b] != "B":
                        w_index += 1
                    if board[a][b] != "W":
                        b_index += 1
        result = min(result, w_index, b_index)
print(result)