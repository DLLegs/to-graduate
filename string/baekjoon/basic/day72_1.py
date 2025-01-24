# 백준 7785번 (복습)

import sys
input = sys.stdin.read

logs =[log for log in input().splitlines() if log.strip()]

employees = set()

for log in logs:
    parts = log.split()
    if len(parts) == 2:
        name, action = parts
        if action == "enter":
            employees.add(name)
        elif action == "leave":
            employees.discard(name)

for name in sorted(employees, reverse=True):
    print(name)

# 백준 10816번 문제

import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
had = list(map(int, data[1:N+1]))
M = int(data[N+1])
cards = list(map(int, data[N+2:]))

card_count = {}
for num in had:
    card_count[num] = card_count.get(num, 0)+1

result = [str(card_count.get(card, 0)) for card in cards]

print(' '.join(result))