# 백준 10886번 문제

join_people = int(input())
cye = 0

for i in range (join_people):
    num = int(input())

    if num == 0 :
        cye -= 1
    else:
        cye += 1
    
if cye < 0:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

# 백준 5086번 문제

while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break
    
    elif B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")
    
# 백준 5717번 문제

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A + B)