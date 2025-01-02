# 백준 9012번 문제

n = int(input())  # 테스트 케이스 수 입력

for _ in range(n):
    result = list(input())  # 괄호 문자열을 리스트로 변환
    stack = []  # 스택 초기화
    is_vps = True  # 초기 상태는 VPS(True)로 가정

    for char in result:
        if char == '(':  # 열림 괄호인 경우 스택에 추가
            stack.append(char)
        elif char == ')':  # 닫힘 괄호인 경우
            if stack:  # 스택이 비어 있지 않으면 pop
                stack.pop()
            else:  # 스택이 비어 있으면 VPS가 아님
                is_vps = False
                break

    # 모든 괄호 처리 후 스택이 비어 있어야 올바른 VPS
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
