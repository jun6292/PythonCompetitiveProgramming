# https://www.acmicpc.net/problem/1654
# 백준 1654 랜선 자르기
# 이진탐색

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

start = 1
end = max(cables)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for c in cables:
        cnt += c // mid

    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)