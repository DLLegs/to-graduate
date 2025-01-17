# 백준 18870번 문제
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
lists = list(map(int, data[1:]))

sorted_lists = sorted(set(lists))

index_map = {value: idx for idx, value in enumerate(sorted_lists)}

compressed_lists = [index_map[x] for x in lists]

print(' '.join(map(str, compressed_lists)))