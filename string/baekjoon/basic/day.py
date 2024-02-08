# 백준10102번 문제

judge = int(input())
votes = input()
count_A = votes.count("A")
count_B = votes.count("B")


if count_A > count_B:
        print("A")
elif count_A < count_B:
        print("B")
else:
        print("Tie")