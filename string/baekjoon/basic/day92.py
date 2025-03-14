# 백준 2475번

# 하드 코딩?
a, b, c, d, e = map(int, input().split())
a = a**2
b = b**2
c = c**2
d = d**2
e = e**2
sum = a+b+c+d+e
print(sum%10)

# for문
nums = list(map(int, input().split()))
result = 0
for num in nums:
    result += num**2
print(result%10)