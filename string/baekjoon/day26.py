# 백준 10817번 문제
# 3개의 정수
# 두 번째로 큰 정수를 출력

# num_list = list(map(int, input().split()))
# num_list.sort()
# print(num_list[1])

# 백준 11653번 문제
# 하나의 정수
# 소인수분해한 결과

# n = int(input())
# i = 2
# while n != 1:
#     if n % i == 0:
#         print(i)
#         n = n/i
#     else:
#         i += 1

# # 백준 1789번 문제
# # 입력값: 자연수
# # 출력값: 자연수가 나오기 위한 서로 다른 자연수

# n = int(input())
# i = 0
# cnt = 0
# while True:
#     if n > i:
#         i += 1
#         n = n - i
#         cnt += 1
#     else:
#         print(cnt)
#         break

# 백준 10039번 문제
# 입력값: 5명의 점수값(5의 배수)
# 출력값: 평균 점수

# total = 0
# for i in range(5):
#     tmp = int(input())
#     if tmp < 40:
#         total += 40
#     else:
#         total += tmp
# print(int(total/5))