# 백준 11651번 문제

import sys # 대량으로 입력 받기 위해서
input = sys.stdin.read # 한번에 입력 받음
data = input().splitlines() # 줄 별로 분할

n = int(data[0]) # 첫 번째 줄에는 좌표의 개수

list = []
for i in range(1, n+1):
    x, y = map(int, data[i].split())
    list.append((x, y)) # 줄 별로 튜플로 저장

# key: sort 메소드의 정렬 기준 설정
# lambda: 간단한 익명 함수 생성
list.sort(key=lambda point: (point[1], point[0]))

for x, y in list:
    print(x, y)