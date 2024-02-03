# 왕실의 나이트
# location = input()
# result = 0
#
# if 'c' <= location[0] <= 'f' and '3' <= location[1] <= '6':
#     result = 8
# elif (location[0] < 'c' and '3' <= location[1] <= '6') or (location[0] > 'f' and '3' <= location[1] <= '6') or \
#             (location[1] < '3' and 'c' <= location[0] <= 'f') or (location[1] > '6' and 'c' <= location[0] <= 'f'):
#     result = 6
# elif (location[0] == 'a' and '3' <= location[1] <= '6') or (location[0] == 'h' and '3' <= location[1] <= '6') or \
#         (location[1] == '1' and 'c' <= location[0] <= 'f') or (location[1] == '8' and 'c' <= location[0] <= 'f') or \
#         (location[0] == 'b' and location[1] == '2') or (location[0] == 'g' and location[1] == '2') or \
#         (location[0] == 'b' and location[1] == '7') or (location[0] == 'g' and location[1] == '7'):
#     result = 4
# elif (location[0] == 'a' and location[1] == '1') or (location[0] == 'h' and location[1] == '1') or \
#         (location[0] == 'a' and location[1] == '8') or (location[0] == 'h' and location[1] == '8'):
#     result = 2
# else:
#     result = 3
#
# print(result)

# 교재 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
