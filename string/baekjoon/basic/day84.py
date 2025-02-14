# # 백준 2164번 파이썬
from collections import deque

N = int(input())

queue = deque(range(1, N+1))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

# 백준 18258번 복습

import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
Queue = deque()
result = []

for i in range(1, n+1):
    cmd = data[i].split()

    if cmd[0] == 'push':
        Queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        result.append(str(Queue.popleft()) if Queue else '-1')
    elif cmd[0] == 'size':
        result.append(str(len(Queue)))
    elif cmd[0] == 'empty':
        result.append(str('1' if not Queue else '0'))
    elif cmd[0] == 'front':
        result.append(str(Queue[0] if Queue else '-1'))
    elif cmd[0] == 'back':
        result.append(str(Queue[-1] if Queue else '-1'))

sys.stdout.write("\n".join(result)+"\n")