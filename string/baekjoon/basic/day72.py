# 백준 7785번

import sys
input = sys.stdin.read

# 입력 처리
# splitlines은 줄 단위로 나눠 리스트로 변환
# if log.strip() 빈 줄 제거
# 해당 조건들을 다 만족시킨 후 log에 입력
logs = [log for log in input().splitlines() if log.strip()]  

# 회사에 남아 있는 직원들을 관리할 집합
employees = set()

for log in logs:
    # parts에 이름, 상태가 그냥 다 따로 들어감
    # ex) parts = ["Baha", "enter"...]
    parts = log.split()
    if len(parts) == 2:  # 형식 검증
        # 리스트 언패킹
        # 리스트이기 때문에 각 요소를 여러 변수에 할당가능
        name, action = parts
        if action == "enter":
            employees.add(name)
        elif action == "leave":
            employees.discard(name)

# 결과 출력 (사전 역순 정렬)
for name in sorted(employees, reverse=True):
    print(name)

# 백준 10815번 (복습)

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
cards = set(map(int, data[1:n+1]))
m = int(data[n+1])
had = set(map(int, data[n+2:]))

# 리스트 컨프리헨션
# for문을 먼저 실행 had 리스트를 순회하며, 각 요소를 card에 할당
# 할당된 card가 cards에 포함되어 있는 지 확인
result = ['1' if card in cards else '0' for card in had]
print(' '.join(result))