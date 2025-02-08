# 백준 28278 문제
# NZEC 에러 발생

import sys

# 빠른 입력 처리
input = sys.stdin.read
commands = input().splitlines()

# 입력이 없는 경우 예외 처리
if not commands:
    sys.exit(0)

try:
    N = int(commands[0])  # 첫 번째 줄: 명령어 개수
except ValueError:
    sys.exit(0)  # 첫 번째 입력이 숫자가 아니면 종료

stack = []
result = []

# 명령어 처리
for i in range(1, min(N + 1, len(commands))):  # ✅ 범위 오류 방지
    cmd = commands[i].split()

    if not cmd:  # ✅ 빈 줄 방지
        continue

    if cmd[0] == '1':  # ✅ 문자열 비교로 수정
        if len(cmd) > 1:  # ✅ 값이 존재하는지 확인
            stack.append(int(cmd[1]))
    elif cmd[0] == '2':
        result.append(str(stack.pop()) if stack else '-1')
    elif cmd[0] == '3':
        result.append(str(len(stack)))
    elif cmd[0] == '4':
        result.append('1' if not stack else '0')
    elif cmd[0] == '5':
        result.append(str(stack[-1]) if stack else '-1')

# 빠른 출력 최적화
sys.stdout.write("\n".join(result) + "\n")
