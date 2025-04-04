# https://www.acmicpc.net/problem/1931
# 백준 1931 회의실 배정
# 각 회의가 겹치지 않게 회의실을 사용할 수 있는 회의의 최대 개수
# 그리디로 해결 가능
# 먼저 회의를 끝나는 시간 기준으로 정렬 / 회의가 빠른 시간에 끝나야 가장 많은 회의를 할 수 있음, 소요 시간이 아님
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각
# 끝나는 시간이 같다면 더 일찍 시작하는 회의순으로 정렬이 필요

n = int(input())
answer = 0
time_list = []

for _ in range(n):
    start_time, end_time = map(int, input().split())
    time_list.append((start_time, end_time))

time_list.sort(key = lambda x : (x[1], x[0]))   # 끝나는 시간으로 오름차순 정렬 후 시작 시간으로 오름차순 정렬

answer += 1
end = time_list[0][1]   # 첫 회의

for i in range(1, n):   # 첫 회의 끝나는 시간보다 먼저 시작하는 회의 제거
    if end > time_list[i][0]:
        continue
    end = time_list[i][1]
    answer += 1


print(answer)
