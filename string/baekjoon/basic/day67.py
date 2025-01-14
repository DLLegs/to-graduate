# 백준 10814번 문제

import sys
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])

list = []
for i in range(1, n+1):
    old, name = data[i].split()
    old = int(old)
    list.append((old, name))

list.sort(key=lambda rule: rule[0])

for old, name in list:
    print(old, name)

# 백준 11650번 문제 복습

N = int(input())

List = []
for i in range(1, N+1):
    x, y = map(int, input().split())
    List.append((x, y))

List.sort(key=lambda sort: (sort[0], sort[1]))

for x, y in List:
    print(x, y)