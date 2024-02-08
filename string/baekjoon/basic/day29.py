# 백준 7567번 문제

dish = input()
heigh = 10

for i in range(1, len(dish)):
    if dish[i] == dish[i-1]:
        heigh += 5
    else:
        heigh += 10
print(heigh)

# 백준 5063번 문제

test_case = int(input())

for i in range(test_case):
    r, e, c = map(int, input().split())
    a = e -c
    if r < a:
        print("advertise")
    elif r == a:
        print("does not matter")
    else:
        print("do not advertise")