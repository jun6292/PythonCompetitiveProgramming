# https://www.acmicpc.net/problem/2003
# 백준 2004 수들의 합 2

n, m = map(int, input().split())
arr = list(map(int, input().split()))

interval_sum = 0
count = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += arr[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= arr[start]

print(count)

