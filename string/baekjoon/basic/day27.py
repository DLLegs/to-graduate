# 백준 1934번 문제
# 입력값: 줄 개수, 두 수
# 출력값: 두 수의 최소 공배수

# import math

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a%b
#     return a # b가 0이 되었을때 최대공약수 return
# def lcm(a, b):
#     return a * b // gcd(a, b) # 두 수의 곱에서 최대공약수를 나누면 최소공배수

# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     if A < B:
#         A, B = B, A
#     result = lcm(A, B)
#     print(result)

# 백준 4101번 문제
# 입력값: 두 수
# 출력값: 첫 번째 수의 큰지 작은지 여부 Yes, No

# while 1:
#     fir, sec = map(int, input().split())
#     if fir > sec:
#         print("Yes")
#     elif fir == 0 and sec == 0:
#         break
#     else:
#         print("No")

# 백준 10156번 문제
# 입력값: 과자 한 개 가격, 과자 개수, 현재 돈
# 출력값: 부모님한테 받아야 하는 돈

# K, N, M = map(int, input().split())
# SMM = 0

# SMM = M - (K * N)

# if SMM < 0:
#     print(-SMM)
# else:
#     print(0)
