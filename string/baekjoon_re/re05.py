# 백준5597번 (1차원 배열)
stu = []

for _ in range(28):
    stu.append(int(input()))

for i in range(1, 31):
    if i not in stu:
        print(i)

# 백준 1546번 (1차원 배열)

N = int(input())
grade = list(map(int, input().split()))
max_grade = max(grade)

res = [(score/max_grade)*100 for score in grade]
average = sum(res)/N
print(average)