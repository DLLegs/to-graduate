# # 백준 24266번

# n = int(input())
# print(n**3)
# print(3)

# 백준 24267번
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

n = int(input())
print(int(((n-2)*(n-1)*(2*n-3) + 3*(n-2)*(n-1)) / 12))
print(3)