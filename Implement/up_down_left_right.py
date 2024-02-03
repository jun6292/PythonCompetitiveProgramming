# 상하좌우 - 나의 풀이
N = int(input())
move_list = list(input().split())
x, y = 1, 1

for move in move_list:
    if move == 'R' and y < N:
        y += 1
    elif move == 'L' and y > 1:
        y -= 1
    elif move == 'U' and x > 1:
        x -= 1
    elif move == 'D' and x < N:
        x += 1

print(x, y)

# 교재 풀이
# n = int(input())
# x, y = 1, 1
# plans = input().split() # 문자열을 공백 기준으로 끊어서 입력 받기
# 
# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
# 
# # 이동 계획을 하나씩 확인
# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
# 
# print(x, y)
