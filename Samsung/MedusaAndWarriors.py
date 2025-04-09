# https://www.codetree.ai/ko/frequent-problems/problems/medusa-and-warriors/description
# 코드트리 메두사와 전사들
from collections import deque

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

n, m = map(int, input().split())
sy, sx, ey, ex = map(int, input().split())  # 메두사 위치, 공원 위치
tmp_list = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]   # 도로 정보 - 도로 0, 비도로 1

warriors = []  # 전사들 위치
for i in range(0, m * 2, 2):
    warriors.append([tmp_list[i], tmp_list[i + 1]])

def bfs(si, sj, ei, ej):    # 메두사 집부터 공원까지 최단 route 찾기
    q = deque()
    visited = [[0] * n for _ in range(n)]

    q.append((si, sj))
    visited[si][sj] = (si, sj)    # 직전 위치를 저장

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):    # 목적지 도착, 경로 저장
            route = []
            ci, cj = visited[ci][cj]
            while (ci, cj) != (si, sj): # 출발지가 아니라면 저장, 출발지는 경로에 필요 없다
                route.append((ci, cj))
                ci, cj = visited[ci][cj]
            return route[::-1]  # 메두사 이동순서대로 역순을 반환

        # 4방향(상하좌우), 범위내, 미방문, 조건(==0)
        for d in range(4):
            ni, nj = ci + dy[d], cj + dx[d]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                # visited에 바로 직전 좌표를 넣어서 경로를 추적할 수 있게.
                visited[ni][nj] = (ci, cj)
    # 이곳까지 왔다는 얘기는 목적지를 못찾았다는 뜻
    return -1

def mark_line(v, ci, cj, dr):   # 일직선으로 안전하다는 표시
    while 0 <= ci < n and 0 <= cj < n:
        v[ci][cj] = 2
        ci, cj = ci + di[dr], cj + dj[dr]

def mark_safe(v, si, sj, dr, org_dr):
    # 직선 방향 표시
    ci, cj = si + di[dr], sj + dj[dr]
    mark_line(v, ci, cj, dr)    # v에 dr 방향으로 이동 가능지역 표시

    # 바라보는 방향으로 한줄씩 표시 - 대각선 방향으로 이동하면서
    ci, cj = si + di[org_dr], sj + dj[org_dr]
    while 0 <= ci < n and 0 <= cj < n:
        mark_line(v, ci, cj, dr)
        ci, cj = ci + di[org_dr], cj + dj[org_dr]

def make_stone(tarr, mi, mj, mdr):
    vf = [[0] * n for _ in range(n)]
    cnt = 0
    # mdr 방향으로 전사 만날 때까지 1 표시, 이후 2 표시
    ni, nj = mi + di[mdr], mj + dj[mdr]
    while 0 <= ni < n and 0 <= nj < n:  # 범위 내라면 계속 진행
        vf[ni][nj] = 1
        if tarr[ni][nj] > 0:
            cnt += tarr[ni][nj]
            ni, nj = ni + di[mdr], nj + dj[mdr]
            mark_line(vf, ni, nj, mdr)  # v에 dr 방향으로 이동가능 지역 표시
            break
        ni, nj = ni + di[mdr], nj + dj[mdr]

    # mdr - 1, mdr + 1 방향으로 동일한 처리, 대각선 원점 잡고 mdr 방향 처리
    for org_dr in ((mdr - 1) % 8, (mdr + 1) % 8):
        si, sj = mi + di[org_dr], mj + dj[org_dr]   # 첫 대각선 위치 체크
        while 0 <= si < n and 0 <= sj < n:  # 대각선 방향으로 초기 위치 탐색 후 직선단위 처리
            if vf[si][sj] == 0 and tarr[si][sj] > 0:    # 전사 만나면 전사가 바라보는 방향 처리
                vf[si][sj] = 1  # 시야처리
                cnt += tarr[si][sj]     # 돌로 만든 전사 수 누적
                mark_safe(vf, si, sj, mdr, org_dr)  # vf에 mdr 방향으로 이동가능 지역 표시
                break

            ci, cj = si, sj # 첫 위치가 전사가 아닌 경우 직선으로 내려오며 탐색
            while 0 <= ci < n and 0 <= cj < n:
                if vf[ci][cj] == 0:
                    vf[ci][cj] = 1   # 시야처리
                    if tarr[ci][cj] > 0:    # 전사가 있다면
                        cnt += tarr[ci][cj] # 전사 돌로 만들고 돌로 만든 전사 수 누적
                        mark_safe(vf, ci, cj, mdr, org_dr)   # vf에 mdr 방향으로 이동가능 지역 표시
                        break
                else:
                    break
                ci, cj = ci + di[mdr], cj + dj[mdr]

            si, sj = si + di[org_dr], sj + dj[org_dr]   # 시작 지점 기준으로 이동

    return vf, cnt

def move_warrior(vf, mi, mj):
    # 1) 상하좌우, 2) 좌우상하 메두사 시야가 아니면 (!= 1) 움직임
    move, attack = 0, 0

    # 첫 번째 이동 후 두 번째 이동
    for dirs in (((-1, 0), (1, 0), (0, -1), (0, 1)), ((0, -1), (0, 1), (-1, 0), (1, 0))):
        for idx in range(len(warriors) - 1, -1, -1): # 모든 전사에 대해
            ci, cj = warriors[idx]  # 현재 전사의 좌표를 꺼내서
            if vf[ci][cj] == 1:  # 메두사 시야면 넘어감
                continue

            dist = abs(mi - ci) + abs(mj - cj)  # 메두사와 현재거리
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                # 범위 내, 메두사 시야 아니고 현재보다 줄어드는 방향으로 이동
                if 0 <= ni < n and 0 <= nj < n and vf[ni][nj] != 1 and dist > abs(mi - ni) + abs(mj - nj):
                    if (ni, nj) == (mi, mj):    # 메두사 좌표인 경우 메두사 공격 후 전사 삭제
                        attack += 1
                        warriors.pop(idx)
                    else:
                        warriors[idx] = [ni, nj]
                    move += 1
                    break

    return move, attack


medusa_route = bfs(sy, sx, ey, ex)
if medusa_route == -1:
    print(-1)
else:
    for my, mx in medusa_route:
        # 메두사 이동: 지정된 최단 거리로 한 칸 이동, 전사 좌표 겹치면 삭제
        # 삭제 시 역순으로 접근하는게 유리
        for i in range(len(warriors) - 1, -1, -1):
            if warriors[i] == [my, mx]: # 메두사 이동 시 전사가 있는 좌표와 겹치면 삭제
                warriors.pop(i)

        # 메두사 시선: 상하좌우 중 전사를 가장 많이 돌로 만들 수 있는 방향
        # => v에 표시해서 이동시 참조(메두사 시선 == 1, 전사에 가려진 곳 == 2, 빈 땅 == 0)
        # warr[][]: 지도에 있는 전사 수 표시
        warr = [[0] * n for _ in range(n)]
        for ty, tx in warriors:
            warr[ty][tx] += 1

        max_stone = -1
        v = []
        for dr in (0, 4, 6, 2): # 상하좌우 순서로 처리
            tmp_v, tmp_stone = make_stone(warr, my, mx, dr)
            if max_stone < tmp_stone:
                max_stone = tmp_stone
                v = tmp_v

        # 전사들 이동(한 칸씩 두번), 메두사 있는 경우 공격
        warriors_move_sum, warriors_attack = move_warrior(v, my, mx)

        print(warriors_move_sum, max_stone, warriors_attack)
    print(0)