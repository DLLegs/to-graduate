# 백준 18258번 문제

import sys
from collections import deque

input = sys.stdin.read
commands = input().splitlines()

N = int(commands[0])
queue = deque()
result = []

for i in range(1, N + 1):
    cmd = commands[i].split()

    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        result.append(str(queue.popleft()) if queue else -1)
    elif cmd[0] == 'size':
        result.append(str(len(queue)))
    elif cmd[0] == 'empty':
        result.append('1' if not queue else '0')
    elif cmd[0] == 'front':
        result.append(str(queue[0]) if queue else '-1')
    elif cmd[0] == 'back':
        result.append(str(queue[-1]) if queue else '-1')

sys.stdout.write("\n".join(map(str,result)) + '\n')