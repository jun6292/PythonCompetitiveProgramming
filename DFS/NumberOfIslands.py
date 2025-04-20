# https://www.acmicpc.net/problem/4963
# 백준 4963 섬의 개수
# DFS
# visited 배열 사용 안함 -> 섬이 1, 바다가 0이므로, 섬 방문 시 0으로 바꿔주면 되기 때문
# 인접행랼

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)  # 재귀의 한계 풀어주기, 백준 채점 서버는 1000으로 제한되어 있기 때문

# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dy = (-1, 1, 0, 0, -1, 1, -1, 1)
dx = (0, 0, -1, 1, -1, -1, 1, 1)

def dfs(y, x):
    map_arr[y][x] = 0
    for i in range(8):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < h and 0 <= nx < w:
            if map_arr[ny][nx]:
                dfs(ny, nx)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    map_arr = []
    island_cnt = 0

    for _ in range(h):
        map_arr.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if map_arr[i][j] == 1:   # 섬이면
                island_cnt += 1
                dfs(i, j)

    print(island_cnt)