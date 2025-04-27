# https://www.acmicpc.net/problem/14889
# 백준 14889 스타트와 링크
# https://www.codetree.ai/ko/frequent-problems/problems/three-at-dawn-and-four-at-dusk/description
# 코드트리 조삼모사

# n명 - 짝수, 능력치 S, 팀의 능력치는 팀에 속한 모든 쌍의 능력치
# 스타트 팀과 링크 팀의 능력치 차이를 최소로

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
team = [0] * n
answer = float("INF")

def dfs(depth):
    global answer
    if sum(team) == n // 2: # 두 팀으로 나눴으면
        start = link = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                cnt = team[i] + team[j]
                if cnt == 0:
                    start += arr[i][j] + arr[j][i]
                elif cnt == 2:
                    link += arr[i][j] + arr[j][i]
        answer = min(answer, abs(start - link)) # 팀 능력치 차이 계산하고 업데이트

    for i in range(depth, n):
        team[i] = 1
        dfs(i + 1)
        team[i] = 0

dfs(0)
print(answer)

