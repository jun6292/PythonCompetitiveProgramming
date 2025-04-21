# https://www.acmicpc.net/problem/2178
# 백준 2178 미로 탐색
# BFS, 인접행랼
from collections import deque

n, m = map(int, input().split())
dy = (-1, 1, 0, 0)  # 상, 하, 좌, 우
dx = (0, 0, -1, 1)

maze_arr = []
for _ in range(n):
    maze_arr.append(input())

visited = [[-1 for _ in range(m)] for _ in range(n)]    # 방문 체크 및 누적

def bfs():
    visited[0][0] = 1   # (0, 0)에서 시작

    q = deque()
    q.append((0,0))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if not (0 <= ny < n and 0 <= nx < m):
                continue

            if maze_arr[ny][nx] == '1' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

bfs()
print(visited[n - 1][m - 1])