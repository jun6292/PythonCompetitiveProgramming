# 1이 될 때까지
# N, K = map(int, input().split())
# result = 0
#
# while True:
#     if N == 1:
#         break
#     if N % K == 0:
#         N = N // K
#     else:
#         N -= 1
#     result += 1
#
# print(result)

# 교재 풀이 1
# n, k = map(int, input().split())
# result = 0
#
# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n //= k
#     result += 1
#
# while n > 1:
#     n -= 1
#     result += 1
#
# print(result)

# 교재 풀이 2
n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += n - target
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += n - 1
print(result)
