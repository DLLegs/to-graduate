# 백준 2558번 문제
# 입력값: 두 정수
# 출력값: 두 정수의 합

# A = int(input())
# B = int(input())
# print(A+B)

# 백준 2163번 문제
# 입력값: 두 정수
# 출력값: 쪼개는 횟수

# a, b = map(int, input().split())

# print(a*b-1)

# 백준 2914번 문제

# song, cR = map(int, input().split())

# cRt = cR -1
# print(song*cRt + 1)

# 백준 2476번 문제

# join_people = int(input())
# list = []

# for i in range(join_people):
#     a, b, c = map(int, input().split())
#     if (a == b and b == c):
#         reward = 10000 + a * 1000
#     elif (a == b or a == c):
#         reward = 1000 + a * 100
#     elif (b == c):
#         reward = 1000 + b * 100
#     else:
#         reward = max(a, b, c) * 100
#     list.append(reward)

# print(max(list))

# 백준 3009번 문제 ***

# points = []
# for _ in range(3): # 변수가 필요없는 반복문일때 _
#     x, y = map(int, input().split())
#     points.append((x, y)) # 튜플 형태로 받기 위해서

# x4, y4 = 0, 0
# for i in range(3):
#     x4 ^= points[i][0] # XOR 비트연산자 중복되지 않는 값 찾기
#     y4 ^= points[i][1]
# print(x4, y4)

# 백준 2754번 문제

# dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7',
#        'B+':'3.3', 'B0':'3.0', 'B-':'2.7',
#        'C+':'2.3', 'C0':'2.0', 'C-':'1.7',
#        'D+':'1.3', 'D0':'1.0', 'D-':'0.7',
#        'F':'0.0'}
# grade = input()
# print(dic[grade])