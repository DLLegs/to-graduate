# 백준 1152번 문제
# 입력값: 문자열
# 출력값: 문자열의 길이(공백 기준)

# strlong = list(map(str,input().split()))
# print(len(strlong))

# 백준 2908번 문제
# 입력값: 같지 않은 세자리수 두 개
# 출력값: 큰 수를 거꾸로 출력

# A, B = input().split()

# A, B = A[::-1], B[::-1]
# print(max(int(A),int(B)))

# 백준 5622번 문제
# 입력값: 영어 문자열
# 출력값: 전화를 걸기 위한 시간

alp_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for uni in alp_list:
    for i in uni:
        for j in word:
            if i == j:
                time += alp_list.index(uni) + 3
print(time)