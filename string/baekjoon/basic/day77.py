# # 백준 2485번 문제

# import sys
# import math
# input = sys.stdin.read
# data = list(map(int, input().split()))
# n = (data[0])
# tree = data[1:n+1]

# gaps = []
# for i in range(1,n):
#     gaps.append(tree[i]-tree[i-1])

# gcd_value = gaps[0]
# for gap in gaps[1:]:
#     gcd_value = math.gcd(gcd_value, gap)

# tree_place = 0
# for gap in gaps:
#     tree_place += (gap//gcd_value)-1

# print(tree_place)

# 백준 1735번 복습

import math

A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

num = A1*B2 + B1*A2
denum = A2*B2

gcd = math.gcd(num, denum)

num = num // gcd
denum = denum // gcd

print(num, denum)