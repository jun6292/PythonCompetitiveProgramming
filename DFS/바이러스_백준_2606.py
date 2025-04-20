# https://www.acmicpc.net/problem/2606
# 바이러스 백준 2606

# 1번 컴퓨터가 웜 바이러스에 걸렸다.
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False] * (n + 1)

def dfs(num):
    global answer
    visited[num] = True
    answer += 1

    for i in arr[num]:
        if not visited[i]:
            dfs(i)

answer = 0
dfs(1)
# 1을 제외하고 세기
print(answer - 1)
