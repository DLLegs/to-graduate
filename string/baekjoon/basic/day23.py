# 백준 2745번 문제
# 입력값: A~Z, 2~36까지
# 출력값: 앞 알파베슬 뒤 숫자로 진법변환

# A, N = input().split()
# ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# A = A[::-1]
# result = 0

# for i,n in enumerate(A):
#     result += (int(N)**i)*(ary.index(n))
# print(result)

# 백준 11005번 문제
# 입력값: 숫자열, 진법
# 출력값: 문자열

Alp, N_before = input().split()
ary_li ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

re_result = ''
Alp = int(Alp)
N_before = int(N_before)

while Alp:
    re_result += ary_li[Alp % N_before]
    Alp//=N_before
print(re_result[::-1])