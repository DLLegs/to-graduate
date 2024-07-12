# 백준 10773번 문제

n = int(input())

stack = []

for _ in range(n):
    N = int(input())
    if N == 0:
        stack.pop()
    else:
        stack.append(N)

print(sum(stack))