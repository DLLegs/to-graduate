# 5086번 (약수, 배수)

while(1):
    a, b = map(int, input().split())
    
    if a == 0 & b == 0:
        break
    elif b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')