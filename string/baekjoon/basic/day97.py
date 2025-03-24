# 백준 24511번 실패

# 총 N개의 자료구조의 개수
# 0: Queue, 1: Stack
# M: 삽입할 수열의 길이
# C: 삽입할 수열

N = int(input())
structure = list(map(int, input().split()))
initial_values = list(map(int, input().split()))
M = int(input())
insert_values = list(map(int, input().split()))

# Step 1️⃣ : Stack 초기값 저장
stack_values = []

for i in range(N):
    if structure[i] == 1:
        stack_values.append(initial_values[i])

# Step 2️⃣ : Stack 개수에 따라 삽입값 처리
if len(stack_values) % 2 == 0:
    # Stack 개수 짝수 → 삽입값 순서 그대로 출력
    print(*insert_values)
else:
    # Stack 개수 홀수 → 삽입값 뒤집어서 출력
    print(*insert_values[::-1])
