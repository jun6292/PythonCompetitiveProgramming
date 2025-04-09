# https://www.codetree.ai/ko/frequent-problems/problems/ancient-ruin-exploration/description
# 마법의 숲 탐색 코드트리

from collections import deque
# 북, 동, 남, 서
# 0, 1, 2, 3
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c, k = map(int, input().split()) # row, col, 정령의 수
unit = [list(map(int, input().split())) for _ in range(k)]
arr = [[0] * (c + 2) for _ in range(r + 4)]   # 마법의 숲 만들고
# 경계 설정하기 => 1은 경계  / U: 위 쪽이 뚫린 경계 형성
for i in range(len(arr) - 1):
    arr[i][0] = 1
    arr[i][c + 1] = 1
for i in range(len(arr[0])):
    arr[r + 3][i] = 1

def arr_init(): # 마법의 숲 초기화
    global arr
    for y in range(0, len(arr) - 1):
        for x in range(1, len(arr[0]) - 1):
            arr[y][x] = 0

# print(arr)
answer = 0
unit_cnt = 2    # 골렘 표시, 구분을 위해 1씩 증가
exit_set = set()

def bfs(sy, sx):
    q = deque()
    visited = [[0] * (c + 2) for _ in range(r + 4)]
    max_y = 0   # -2해서 return => 맨 위가 뚤려서 3부터 시작이니

    q.append((sy, sx))
    visited[sy][sx] = 1

    while q:
        cy_, cx_ = q.popleft()
        max_y = max(cy_, max_y)

        # 4방향, 미방문, 조건: 값은 값 또는 내가 출구에 있고 상대방이 골렘
        for d in range(4):
            ny, nx = cy_ + dy[d], cx_ + dx[d]
            # 미방문 and 내가 출구에 있고 상대방이 골렘
            if visited[ny][nx] == 0 and (arr[cy_][cx_] == arr[ny][nx] or ((cy_, cx_) in exit_set and arr[ny][nx] > 1)):
                q.append((ny, nx))
                visited[ny][nx] = 1
    return max_y - 2

# 골렘 입력 좌표(cx)/방향(dr)에 따라서 남쪽이동 및 정령 최대 좌표 계산
for cx, dr in unit:
    cy = 1  # 골렘의 중심
    while True:
        # 남쪽으로 최대한 이동(남쪽 -> 서쪽 -> 동쪽)
        if arr[cy + 2][cx] == 0 and arr[cy + 1][cx - 1] == 0 and arr[cy + 1][cx + 1] == 0:    # 비어있다
            cy += 1
        # 서쪽으로 반시계 회전하면서 아래로 한칸
        elif arr[cy][cx - 2] == 0 and arr[cy - 1][cx - 1] == 0 and arr[cy + 1][cx - 1] == 0 and arr[cy + 2][cx - 1] == 0 and arr[cy + 1][cx - 2] == 0:
            cy += 1
            cx -= 1
            dr = (dr - 1) % 4   # 서쪽으로 회전
        # 동쪽으로 반시계 회전하면서 아래로 한칸
        elif arr[cy][cx + 2] == 0 and arr[cy - 1][cx + 1] == 0 and arr[cy + 1][cx + 1] == 0 and arr[cy + 2][cx + 1] == 0 and arr[cy + 1][cx + 2] == 0:
            cy += 1
            cx += 1
            dr = (dr + 1) % 4   # 동쪽으로 회전
        else:   # 더 이상 남쪽으로 내려갈 수 없음
            break

    # 골렘 정착
    if cy < 4:  # 골렘의 몸이 범위 밖 => 새롭게 탐색 시작, arr 초기화
        arr_init()
        unit_cnt = 2
        exit_set = set()
    # 골렘 표시
    else:
        arr[cy][cx] = arr[cy][cx - 1] = arr[cy][cx + 1] = arr[cy - 1][cx] = arr[cy + 1][cx] = unit_cnt
        unit_cnt += 1
        exit_set.add((cy + dy[dr], cx + dx[dr]))    # 골렘 비상구 위치 추가
        answer += bfs(cy, cx)   # 정령 이동 및 최댓값 누적

print(answer)