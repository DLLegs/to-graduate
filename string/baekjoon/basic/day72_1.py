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