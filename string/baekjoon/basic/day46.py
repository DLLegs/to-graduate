# 백준 2292번 문제

# 규칙...?
# 1 = 6 * 0 + 1   -> '1'
# 5 = 6 * 1 - 1  -> 6 * 1 + '1' = '7'
# 11 = 6 * 2 - 1  -> 6 * 2 + '7' = '19'
# 17 = 6 * 3 - 1  -> 6 * 3 + '19' = 37

N = int(input())
i = 1
round = 1

while N > round:
    round += i * 6
    i += 1

print(i)