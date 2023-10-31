# 백준 10798번 문제
# 입력값: 알파벳 대문자, 소문자, 0~9까지 숫자
# 출력값: 세로로 읽은 긴 문자열

long_word = [input() for i in range(5)]
for j in range(15):
    for i in range(5):
        if j < len(long_word[i]):
            print(long_word[i][j], end = "")

# 백준 2563번 문제
# 입력값: 색종이의 개수, 색종이의 위치
# 출력값: 색종이가 붙은 영역의 넓이

ary = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())

for i in range(N):
    x, y = list(map(int, input().split()))
    for row in range(x, x+10):
        for col in range(y, y+10):
            ary[row][col] = 1

result = 0

for i in ary:
    result += i.count(1)
print(result)