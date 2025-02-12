# 백준 4949번 문제

import sys

def balance(sentences):
    stack = []
    for char in sentences:
        # in 연산자가 ([ 하나의 문자열이지만, 하나씩 비교함
        if char in "([":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return "no"
            stack.pop()
        elif char == "]":
            if not stack or stack[-1] != "[":
                return "no"
            stack.pop()
    
    return "yes" if not stack else "no"


input = sys.stdin.read
sentences = input().splitlines()

result = []
for sentence in sentences:
    if sentence == ".":
        break
    result.append(balance(sentence))

sys.stdout.write("\n".join(result) + "\n")