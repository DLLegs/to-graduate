# 백준 11718번 문제
# 입력값: 문자열
# 출력값: 입력값 그대로

# while True:
#     try:
#         print(input())
#     except EOFError:
#         break

# 백준 25083번 문제
# 입력값: 없음
# 출력값: 그림

# print("         ,r\'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r\'")
# print("   `~\\/")
# print("      |")
# print("      |")

# 백준 3003번 문제
# 입력값: 찾은 체스말의 개수
# 출력값: 정확한 피스 수

# akf = [1,1,2,2,2,8]
# user_input = list(map(int,input().split()))

# for i in range(len(akf)):
#     print(akf[i] - user_input[i], end=' ') #end = '' 줄바꿈 안되게함

# 백준 2444번 문제
# 입력값: 숫자
# 출력값: 1부터 줄바꿈 입력 숫자까지

# a = int(input())
# for i in range(1, a+1):
#     print(" "*(a-i) + "*"*(2*i-1))
# for i in range(a-1,0,-1):
#     print(" "*(a-i) + "*"*(2*i-1))

# 백준 10988번 문제
# 입력값: 영어 문자열
# 출력값: 팰린드롬 1 아니면 0

# what_pl = input()
# if what_pl[::1] == what_pl[::-1]:
#     print(1)
# else:
#     print(0)