# 백준 27866번 문제
# 입력값: 첫째줄 영어 소문자 대문자(앞은 무조건 s), 둘째 줄은 정수
# 출력값: 입력받은 정수에 위치한 문자

# string = input()
# loc = int(input())
# print(string[loc-1])

# 백준 2743번 문제
# 입력값: 문자열
# 출력값: 문자열의 길이

# howlong = input()
# print(len(howlong))

# 백준 9086번 문제
# 입력값: 테스트 횟수, 문자열
# 출력값: 문자열 첫과 끝

# times = int(input())

# for i in range(times):
#     text = input()
#     print(text[0],text[-1],sep='')

# 백준 11654번 문제
# 입력값: 알파벳 소문자, 대문자, 숫자 0~9중 하나 입력
# 출력값: 아스키 코드 값 출력

# X = input()
# print(ord(X))

# 백준 11720번 문제
# 입력값: 입력할 숫자의 개수, 더할 숫자의 리스트
# 출력값: 숫자 리스트의 합

# N = int(input())
# nList = list(input())
# sum = 0

# for i in nList:
#     sum += int(i)
# print(sum)

# 백준 10809번 문제
# 입력값: 임의 문자열
# 출력값: 알파벳 소문자열에 위치하는 인덱스값

# S = input()
# for x in 'abcdefghijklmnopqrstuvwxyz':
#     print(S.find(x), end = ' ')

# 백준 2675번 문제
# 입력값: 총 입력받을 문자열 개수, 반복할 횟수 + 문자열
# 출력값: 반복하는 문자열

many = int(input())
for i in range(many):
    R, S = map(str, input().split())
    R = int(R)
    S = list(S)
    for j in range(len(S)):
        print(S[j]*R, end = '')
    print('')