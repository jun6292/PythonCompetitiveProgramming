# 메모이제이션을 활용한 피보나치 수열, 반복문 사용

dp = [0] * 100

dp[1] = 1
dp[2] = 1
n = 99

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])