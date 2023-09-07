# 백준 2525번 문제
# 입력값: 시작 시간(시:분), 필요한 시간(분)
# 출력값: 끝나는 시간(시:분)
# 시작 시간에 필요한 시간을 더해 끝나는 시간을 (시:분) 형식으로 출력이 필요

hour,min = map(int, input().split()) # 한 줄에 동시에 받는 변수 나누기
plus = int(input())

hour += plus // 60
min += plus % 60

if min >= 60:
    min = min - 60
    hour = hour + 1

if hour >= 24:
    hour = hour - 24

print(hour,min)

# 백준 2480번 문제
# 입력값: 주사위 총 3개의 값
# 출력값: 같은 눈 3개(만원 + 값*천원), 같은 눈 2개(천원 + 값*백원)
# 다른 눈(값*백원)
# 눈의 값을 비교하는 조건문 필요

a,b,c=map(int, input().split())

if a == b == c:
    mon = 10000 + (a * 1000)
elif a == b or b == c:
    mon = 1000 + (b * 100)
elif a == c:
    mon = 1000 + (c * 100)
else:
    mon=max(a,b,c)*100

print(mon)