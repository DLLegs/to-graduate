# 백준 13909번 문제

# 아이디어
# 약수가 홀수개인 숫자의 창문은 열려있음
# 완전제곱수는 약수가 홀수개임
# 2^2, 3^2... => 4(1,2,4), 9(1,3,9)....

man = int(input())
count = 0

for i in range(1, man+1):
    if i**2 <= man:
        count += 1
    else:
        break

print(count)

# # 제곱근 활용 최적화 코드
# # import math
# # mans = int(input())
# # print(math.isqrt(mans))

# 백준 2485번 복습

import sys
import math
input = sys.stdin.read
data = list(map(int, input().split()))
N = data[0]
tree = data[1:]

gaps = []
for i in range(1, len(tree)):
    gaps.append(tree[i]-tree[i-1])

gaps_value = gaps[0]
for gap in gaps:
    gaps_value = math.gcd(gap, gaps_value)

tree_place = 0
for gap in gaps:
    tree_place += (gap//gaps_value) -1

print(tree_place)