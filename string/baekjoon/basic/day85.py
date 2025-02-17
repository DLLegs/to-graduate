# 백준 11866번 문제

N, K = map(int, input().split())
people = list(range(1, N+1))
y_list = []

index = 0

while people:
    index = (index + K-1) % len(people)
    y_list.append(str(people.pop(index)))

print("<"+", ".join(y_list)+">")

# 백준 2164번 복습
from collections import deque

n = int(input())
qeque = deque(range(1, n+1))

while len(qeque) > 1:
    qeque.popleft()
    qeque.append(qeque.popleft())

print(qeque[0])