### 백준 11401번 문제
## 거듭제곱, 모듈로 곱셈 역원, 페르마의 소정리

# 이항계수: 주어진 집합에서 원하는 개수만큼
# 순서없이 뽑는 조합의 개수
# (n) = nCk =    n!      단(0<=k<=n)
# (k)       = (n-k)!k!  

## 함수를 이용한 직접 계산법
import math

def binomial_coefficient(n, k):
    if k > n:
        return 0
    return math.factorial(n) // (math.factorial(n-k)*math.factorial(k))
n, k = 5, 2 # 10
print(binomial_coefficient(n, k))

## 파스칼 삼각형을 이용한 동적 계산법
def binomail_coefficient2(n, k):
    # 테이블 초기화 -> 2차원 리스트 생성
    C = [[0 for _ in range(k+1)] for _ in range(n+1)]
    # 기본 경우 초기화
    for i in range(n+1):
        for j in range(min(i, k)+1): # 불필요한 계산을 방지
            if j == 0 or i == j:
                C[i][j] = 1
            else: # 파스칼 삼각형의 삼각형법
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    
    return C[n][k]

n, k = 5, 2
print(binomail_coefficient2(n,k))

## 페르마의 소정리를 이용한 모듈러 연산
MOD = 1000000007

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i % MOD
    return result

def modular_inverse(a, p):
    # a^(p-2) % p 를 계산하기 위함
    return pow(a, p-2, p)

def binomial_coefficient3(n, k, p):
    if k > n:
        return 0
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n-k) % p
    return numerator * modular_inverse(denominator, p) % p

n, k = 5, 2
print(binomial_coefficient3(n, k, MOD))

## 문제 해결 코드