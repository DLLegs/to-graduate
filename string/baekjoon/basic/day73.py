# 백준 1764번 문제

import sys
input = sys.stdin.read
# 한 줄씩 리스트에 저장
data = input().splitlines()
n, m = map(int, data[0].split())
no_hear = set(data[1:n+1])
no_see = set(data[n+1:n+m+1])

# 교집합을 보고 사전순으로 정렬
no_hear_see = sorted(no_hear & no_see)

print(len(no_hear_see))
print("\n".join(no_hear_see))

# 백준 10816번 문제 복습

import sys
Input = sys.stdin.read()

# 입력 처리
Data = Input.split()
N = int(Data[0])
M = int(Data[N])  

# 숫자 카드 개수 (내가 가진 카드)
had = list(map(int, Data[1:N+1]))

# 확인해야 할 숫자들
cards = list(map(int, Data[N+1:]))

# 카드 개수 카운트
card_count = {}
for num in had:
    # card_count.get에서 있으면 num가져오기 없으면 0
    card_count[num] = card_count.get(num, 0) + 1

# 결과 생성
result = [str(card_count.get(card, 0)) for card in cards]

# 출력
print(" ".join(result)) 