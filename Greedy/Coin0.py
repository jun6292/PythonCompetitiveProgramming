# https://www.acmicpc.net/problem/11047
# 백준 11047 동전
# 동전의 입력 값이 오름차순으로 들어오고, 이전의 입력 값의 배수로만 들어오기 때문에
# 그리디로 해결 가능

n, k = map(int, input().split())
coin = []
answer = 0

for _ in range(n):
    coin.append(int(input()))

for c in coin[::-1]:
    if k == 0:
        break
    answer += k // c
    k %= c

print(answer)
