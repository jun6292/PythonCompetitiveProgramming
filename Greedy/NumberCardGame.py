# 숫자 카드 게임
# N, M = map(int, input().split())
# result = 0
#
# for _ in range(N):
#     card_list = list(map(int, input().split()))
#     min_num = min(card_list)
#     result = max(result, min_num)
#
# print(result)

# 교재 정답
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(min_value, result)

print(result)
