# 백준 1181번 문제

import sys
input= sys.stdin.read
data = input().splitlines()

n = int(data[0])
words =[]

for i in range(1, n+1):
    word = data[i]
    words.append(word)

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)


# 백준 10814번 문제 (복습)

import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
humen = []

for i in range(1, N+1):
    age, name = data[i].split()
    age = int(age)
    humen.append((age, name))

humen.sort(key=lambda rule: rule[0])

for age, name in humen:
    print(age,name)