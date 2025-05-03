# https://www.acmicpc.net/problem/1927
# 최소 힙 백준 1927

# 배열에 자연수 x를 넣는다. => 입력이 자연수면
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. => 입력이 0이면

import heapq
import sys

input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, num)