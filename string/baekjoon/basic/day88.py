# 백준 10872번 문제

N = int(input())
result = 1

if N > 0:
    for i in range(1, N+1):
        result *= i
print(result)

# 재귀 함수
def factorial(n):
    results = 1
    if n > 0:
        results = n * factorial(n-1)

n = int(input())
print(factorial(n))