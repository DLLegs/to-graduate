# 백준 1655번 문제
# 알고리즘 분류: 자료 구조, 우선순의 큐
# 우선순의 큐, 힙(heap) (자료 구조)구현하기
# 최대값과 최솟값을 찾는 연산은 완전이진트리를 이용
# 큐나 스택과 비슷한 자료형이지만, 각 원소들은 우선순위를 가지고 있다
# 우선순위 큐는 힙(heap) 자료 구조를 통해 구현
# 우선순위 큐는 부모노드만 접근 가능함

import heapq
# 그냥 input 사용시 시간초과 문제가 생김
import sys
# 최대 힙과 최소 힙으로 수열을 반으로 나눔
left_heap = []
right_heap = []

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
# 짝수가 되면 작은 수를 중간값으로 가져오기 때문
    if len(left_heap) <= len(right_heap):
        # 최대 힙을 만들기 위해서 '-x' 사용
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)
    # 두 힙에 값이 존재하고 왼쪽 힙의 값이 오른쪽 힙의 값보다 크면 바꿔주기 위한 절차
    if right_heap and -left_heap[0] > right_heap[0]:
        max_value = -heapq.heappop(left_heap)
        min_value = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -min_value)
        heapq.heappush(right_heap, max_value)
    
    print(-left_heap[0])