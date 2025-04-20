# https://www.acmicpc.net/problem/11724
# 백준 11724 연결 요소의 개수
# 인접리스트
import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

cnt = 0
visited = [False for _ in range(n + 1)]

def dfs(start):
    visited[start] = True
    for node in arr[start]:
        if not visited[node]:
            dfs(node)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)