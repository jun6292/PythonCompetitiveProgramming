# https://www.acmicpc.net/problem/14888
# https://www.codetree.ai/ko/frequent-problems/problems/arrange-operator/description
# 백준 14888 연산자 끼워넣기
# 코드트리 연산자 배치하기

n = int(input())
numbers = list(map(int, input().split()))
# calc = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_value, min_value = -float("INF"), float("INF")

# def dfs(num, depth):
#     global max_value, min_value
#
#     if depth == n:
#         max_value, min_value = max(max_value, num), min(min_value, num)
#         return
#
#     for i in range(4):
#         if calc[i] == 0:
#             continue
#         calc[i] -= 1
#         if i == 0:
#             result = num + numbers[depth]
#         elif i == 1:
#             result = num - numbers[depth]
#         elif i == 2:
#             result = num * numbers[depth]
#         else:
#             result = int(num / numbers[depth])
#
#         dfs(result, depth + 1)
#         calc[i] += 1    # 백트래킹의 요소 - 원상복구
#
# dfs(numbers[0], 1)


def dfs(depth, sm, add, sub, mul, div):
    global max_value, min_value
    if depth == n:
        max_value = max(sm, max_value)
        min_value = min(sm, min_value)
        return

    if add > 0:
        dfs(depth + 1, sm + numbers[depth], add - 1, sub, mul, div)
    if sub > 0:
        dfs(depth + 1, sm - numbers[depth], add, sub - 1, mul, div)
    if mul > 0:
        dfs(depth + 1, sm * numbers[depth], add, sub, mul - 1, div)
    if div > 0:
        dfs(depth + 1, int(sm / numbers[depth]), add, sub, mul, div - 1)


dfs(1, numbers[0], add, sub, mul, div)
print(max_value, min_value, sep='\n')