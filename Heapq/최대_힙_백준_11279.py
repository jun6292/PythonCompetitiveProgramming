# https://www.acmicpc.net/problem/11279
# 최대 힙 백준 11279

# 두 연산 지원하는 프로그램 작성
# 1) 배열에 자연수 x를 넣음
# 2) 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거

import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    command = int(input())
    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -command)
