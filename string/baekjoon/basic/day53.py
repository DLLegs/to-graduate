# 백준 1978번 문제
#에라토스테네스의 체 알고리즘으로 해결 가능

n = int(input())
num = list(map(int, input().split()))
result = 0

# 2보다 작으면 소수가 아니므로 건너뜀
for i in num:
    if i < 2:
        continue
# 소수 판별문
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if(i % j == 0):
            is_prime = False
            break
    if is_prime:
        result += 1

print(result)