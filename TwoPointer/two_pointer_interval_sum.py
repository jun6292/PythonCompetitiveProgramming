# 투 포인터 부분합
n, m = map(int, input().split())    # n: 데이터의 갯수, m: 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start를 차례로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)