# 백준 13241번 문제
# 최소 공배수
# 튜플 언패킹
# 오른쪽에 있는 튜플 값을 왼쪽에 차례로 할당하는 것


def gcd(A, B):
    
    while B != 0:
       A, B = B, A % B # 튜플 언패킹: B와 A%B 값을 평가하여 (B, A%B)인 튜플로 만듬
    return A

def lcm(A, B):
    return abs(A*B) // gcd(A,B)

A, B = map(int,input().split())
if A < B:
    temp = A
    A = B
    B = temp

print(lcm(A, B))