# 백준 11650번 문제
# sys.stdin.read 안한 버전

n = int(input())

list = []
for _ in range(n):
    x, y = map(int, input().split())
    list.append((x, y))

list.sort(key=lambda rule: (rule[0], rule[1]))

for x, y in list:
    print(x, y)