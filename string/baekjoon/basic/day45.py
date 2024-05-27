# 백준 2798번 문제

from itertools import combinations

N, M = map(int, input().split())
Card_List = list(map(int, input().split()))

possible_combinatrion = combinations(Card_List, 3) ## 조합 찾아주는 함수

max_sum = 0

for i in possible_combinatrion:
    current_sum = sum(i)
    if current_sum <= M:
        max_sum = max(current_sum, max_sum)
    
print(max_sum)