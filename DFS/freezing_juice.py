# 음료수 얼려 먹기
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1 # 해당 노드 방문
        dfs(x - 1, y)   # 상
        dfs(x + 1, y)   # 하
        dfs(x, y - 1)   # 좌
        dfs(x, y + 1)   # 우
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)

