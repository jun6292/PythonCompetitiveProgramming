# 시각 - 나의 풀이
N = int(input())
result = 0

for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)

# 교재 풀이와 똑같다