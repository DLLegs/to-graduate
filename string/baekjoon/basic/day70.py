# 백준 2751번 문제

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
lists = list(map(int, data[1:]))

lists.sort()

for i in range(n):
    print(lists[i])
# 복습 응용
# print(' '.join(map(str, lists)))

# 백준 18870번 (복습)

import sys
Input = sys.stdin.read
Data = Input().split()
N = int(Input[0])
Lists = list(map(int, Data[1:]))

sorted_list = sorted(set(Lists))

# 딕셔너리 컴프리헨션
# sorted_list 리스트의 값을 값 -> 인덱스 형태로 매핑
# 예시 (익덱스, 값) -> (값, 인덱스) 형태로 매핑
index_list = {value: idx for idx, value in enumerate(sorted_list)}

# 리스트 컴프리헨션
# Lists에 있는 값을 받아와서 index값과 비교
# 알맞은 value값을 compreesed_list에 반환환
compressed_list = [index_list[x] for x in Lists]

print(' '.join(map(str, compressed_list)))