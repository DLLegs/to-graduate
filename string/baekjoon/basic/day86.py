# 백준 28279번 문제
import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
dack = deque()
result = []

for i in range(1, n+1):
    cmd = data[i].split()

    if cmd[0] == '1':
        dack.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        dack.append(int(cmd[1]))
    elif cmd[0] == '3':
        result.append(str(dack.popleft() if dack else '-1'))
    elif cmd[0] == '4':
        result.append(str(dack.pop() if dack else '-1'))
    elif cmd[0] == '5':
        result.append(str(len(dack)))
    elif cmd[0] == '6':
        result.append(str('1' if not dack else '0'))
    elif cmd[0] == '7':
        result.append(str(dack[0] if dack else '-1'))
    elif cmd[0] == '8':
        result.append(str(dack[-1] if dack else '-1'))

sys.stdout.write("\n".join(result)+'\n')

# 백준 2346번 문제

from collections import deque

N = int(input())
# enumerate(객체, 값) 형태로 주로 사용
# 객체에 인덱스를 지정해서 같이 저장해줌
# 인덱스에 첫번째 값은 뒤에 값이 지정
balloons = deque(enumerate(map(int, input().split()), start=1))
Result = []

index, move = balloons.popleft()
Result.append(str(index))

# 모듈러 연산
while balloons:

    if move > 0:
        balloons.rotate(-(move-1))
    else:
        balloons.rotate(-move)
    
    index, move = balloons.popleft()
    Result.append(str(index))

print(" ".join(Result))