# 백준 2292번 문제

x, y, w, h = map(int, input().split())

distance_to_left = x
distance_to_right = w - x
distance_to_top = h - y
distance_to_bottom = y

print(min(distance_to_left,distance_to_right,distance_to_top,distance_to_bottom))

# 백준 14215번 문제

a, b, c = map(int, input().split())
sizes = sorted([a, b, c])

largest = sizes[2]

sum_of_size = sizes[0] + sizes[1]

if largest > sum_of_size:
    print(sum_of_size * 2 - 1)

else:
    print(sizes[0] + sizes[1] + sizes[2])