##MenOfPassion(A[],n){
#     sum < - 0;
#     for i < - 1 to n
#         for j < -1 to n
#             sum < - sum + A[i] * A[j];
#     return sum;
# }

# 시간 복잡도 문제 루프가 2개라서
N = int(input())
print(N**2)
print(2)

n = int(input())
print(int(n*(n-1) - (n-1)*n/2))
print(2)