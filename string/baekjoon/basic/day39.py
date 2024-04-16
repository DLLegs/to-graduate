# 백준 2720번 문제
# 그리디 알고리즘
# 최적해를 구하는 알고리즘
# 동전 거스름돈, 활동 선택, 최단 경로, 배낭 문제에서 많이 나옴

n = int(input())

for _ in range(n):
    money = int(input())
    for i in [25, 10, 5, 1]: # 파이썬은 리스트 순회도 가능
        print(money // i, end = ' ')
        money = money % i

# 백준 2903번 문제

N = int(input())
print((2**N+1)**2)