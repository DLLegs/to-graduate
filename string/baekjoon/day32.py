# # 백준 9506번 문제

# while True:
#     n = int(input())
#     num_list = []
#     total = 0

#     if n == -1:
#         break
#     for i in range(1, n//2 + 1):
#         if n%i == 0:
#             num_list.append(i)
#             total += i
        
#     if total == n:
#         temp = ' + '.join(map(str, num_list))
#         print(f"{n} = {temp}")
#     else:
#         print(f"{n} is NOT perfect.")

# # 백준 10162번 문제

# time = int(input())

# if (time % 10) != 0:
#     print("-1")
# else:

#     A = time//300
#     B = (time%300)//60
#     C = (time%60)//10
#     print(A, B, C)

# # 백준 10103번 문제

# round = int(input())
# Chang, Syang = 100, 100

# for _ in range(round):
#     C_dice, S_dice = map(int, input().split())
#     if C_dice > S_dice:
#         Syang -= C_dice
#     elif S_dice > C_dice:
#         Chang -= S_dice

# print(Chang)
# print(Syang)

# # 벡준 10214번 문제

# case = int(input())

# for _ in range(case):
#     Y = 0
#     K = 0
    
#     for _ in range(9):
#         y, k = map(int, input().split())
#         Y += y
#         K += k

#     if Y > K:
#         print("Yonsei")
#     elif Y < K:
#         print("Korea")
#     else:
#         print("Draw")

## 백준 11557번 문제

