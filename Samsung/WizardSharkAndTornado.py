# https://www.acmicpc.net/problem/20057
# 백준 20057 마법사 상어와 토네이도
# 토네이도는 항상 정가운데에서 시작, (1, 1)까지 이동 후 소멸, 소멸 후 격자 밖으로 나간 모래의 양을 출력
# 방향 좌, 하, 우, 상, 좌, 하, 우, 상 반복
# Cnt 1,  1, 2, 2,  3, 3,  4, 4, ...
#flag 0,  1, 0, 1,  0, 1,  0, 1, ...

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 좌, 하, 우, 상
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

dr = cnt = flag = answer = 0
cnt_max = 1
cy = cx = n // 2 # 토네이도는 중심에서부터 시작

# 0(2%), 1(10%), 2(7%), 3(1%), 4(5%), 5(10%), 6(7%), 7(1%), 8(2%), 9(a)
ay = [[-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0],
      [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]]
ax = [[0, -1, 0, 1, -2, -1, 0, 1, 0, -1],
      [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0]]
mul = [2, 10, 7, 1, 5, 10, 7, 1, 2, 0]

while (cy, cx) != (0, 0):
    cy, cx = cy + dy[dr], cx + dx[dr] # dr 방향으로 한 칸 이동

    # cy, cx 기준 좌표 중심으로 모래량 계산 추가, 범위 밖이면 answer에 추가
    if arr[cy][cx] > 0:     # 모래가 있을때만 진행
        val = arr[cy][cx]   # 기준 좌표 모래양
        arr[cy][cx] = 0     # 기준 좌표 모래는 사라짐
        sand_sum = 0        # 모래양 누적

        for i in range(10): # 0 ~ 9 처리
            ny, nx = cy + ay[dr][i], cx + ax[dr][i] # 10개 좌표 모래양 계산
            tmp = (val * mul[i]) // 100 # 소수점 이하 버림
            if i == 9:
                tmp = val - sand_sum
            if 0 <= ny < n and 0 <= nx < n: # 범위 내 => 누적
                arr[ny][nx] += tmp
            else:   # 밖으로 나간 모래양 추가
                answer += tmp
            sand_sum += tmp

    cnt += 1
    if cnt == cnt_max:
        cnt = 0
        dr = (dr + 1) % 4   # 방향 전환
        if flag == 0:
            flag = 1
        else:
            flag = 0
            cnt_max += 1

print(answer)