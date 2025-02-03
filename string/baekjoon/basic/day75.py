# 백준 11478번 문제

s = input().strip()

substring = set()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substring.add(s[i:j])

print(len(substring))

# 백준 1269번 복습
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())

A = set(map(int, data[1].split()))
B = set(map(int, data[2].split()))

union = A ^ B

print(len(union))