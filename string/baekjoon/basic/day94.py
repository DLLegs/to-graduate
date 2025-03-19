# 백준 7568번 문제

N = int(input())
people = []

for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    print(rank, end=' ')