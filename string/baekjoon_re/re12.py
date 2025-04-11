# 백준 2566번 (2차원 배열)
import sys
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

max_value = matrix[0][0]
max_i, max_j = 0, 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_i = i
            max_j = j

print(max_value)
print(max_i+1, max_j+1)