# 백준 1977번 문제

A = int(input())
B = int(input())
com_list = []  # 조건에 충족하는 값 저장

for i in range(A, B+1):  # 범위
    T = int(i ** 0.5) ** 2  # i를 제곱근후 다시 제곱한 값
    
    if i == T:  # T와 i가 같은지 비교하여 조건에 맞는지 확인
        com_list.append(i)  # 확인후 리스트에 저장

if com_list:  # com_list 비어있는지 확인
    print(sum(com_list))  # 합을 계산하여 출력
    print(min(com_list))  # 최소값을 계산하여 출력
else:
    print(-1)  # 없으면 -1 출력