# 백준 2587번 문제
import math

A = []

for i in range(5):
    A.append(int(input()))
    A.sort()

print(math.trunc(sum(A)/len(A)))
print(A[2])

# 코드 개선
# # 입력 받기
# A = sorted([int(input()) for _ in range(5)])

# # 평균 출력
# print(int(sum(A) / len(A)))

# # 중앙값 출력
# print(A[2])
