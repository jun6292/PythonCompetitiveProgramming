# 게임 개발
N, M = map(int, input().split())
x, y, d = map(int, input().split()) # 방향 d는 0(북쪽), 1(동쪽), 2(남쪽), 3(서쪽)

record = [[0] * M for _ in range(N)]    # 기록용
record[x][y] = 1

game_board = []     # 게임 보드 입력 받기
for _ in range(N):
    game_board.append(list(map(int, input().split())))

move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0(북쪽), 1(동쪽), 2(남쪽), 3(서쪽)으로 이동

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

result = 1   # 처음 시작은 반드시 육지이므로 1부터 카운트
turn_cnt = 0    # 회전 카운트
while True:
    # 현재 방향 기준으로 왼쪽 방향으로 돈다
    turn_left()
    # 새로운 좌표 설정
    new_x = x + move[d][0]
    new_y = y + move[d][1]
    # 육지이고, 가보지 않은 곳이라면
    if record[new_x][new_y] == 0 and game_board[new_x][new_y] == 0:
        # 간다 -> 방문 표시
        record[new_x][new_y] = 1
        # 갔으므로 현재 좌표 재설정하고
        x = new_x
        y = new_y
        # 방문했으므로 1 카운트
        result += 1
        turn_cnt = 0
        continue
    else:
        # 갈 수 없으면 -> 돌아야하므로 회전 횟수 카운트
        turn_cnt += 1
    if turn_cnt == 4:   # 네 방향 모두 막힘 -> 뒤로 가야 함
        new_x = x - move[d][0]
        new_y = y - move[d][1]
        # 뒤가 육지라면? -> 갈 수 있다
        if game_board[new_x][new_y] == 0:
            x = new_x
            y = new_y
        else: # 뒤가 바다라면? -> 움직임을 멈춘다.
            break
        turn_cnt = 0

print(result)
