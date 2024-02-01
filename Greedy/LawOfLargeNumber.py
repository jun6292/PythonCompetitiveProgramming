# 큰 수의 법칙

# N, M, K = map(int, input().split())
# result = 0
#
# numbers = list(map(int, input().split()))
#
# numbers.sort(reverse=True)  # 내림차순 정렬
# first_num = numbers[0]  # 가장 큰 수
# second_num = numbers[1]  # 그 다음 큰 수
#
# add_first_num_cnt = (M // (K + 1)) * K  # 가장 큰 수가 더해지는 횟수
# add_first_num_cnt += M % (K + 1)
#
# result += add_first_num_cnt * first_num
# result += (M - add_first_num_cnt) * second_num
#
# print(result)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)