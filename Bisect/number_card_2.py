# https://www.acmicpc.net/problem/10816
# 숫자 카드 2

# N = int(input())
# num_cards = list(map(int, input().split())) # 상근이가 가지고 있는 숫자 카드
# M = int(input())
# num_arr = list(map(int, input().split()))   # 몇 개 가지고 있는 숫자 카드인지 구해야 할 목록
# answer = []
# num_dict = {}
#
# for num in num_arr:
#     num_dict[num] = 0
#
# for num in num_cards:
#     if num in num_dict.keys():
#         num_dict[num] += 1
#     else:
#         continue
#
# for n in num_arr:
#     if n in num_dict:
#         answer.append(num_dict[n])
#     else:
#         answer.append(0)
#
# print(*answer)

N = int(input())
num_cards = list(map(int, input().split())) # 상근이가 가지고 있는 숫자 카드
M = int(input())
num_arr = list(map(int, input().split()))   # 몇 개 가지고 있는 숫자 카드인지 구해야 할 목록

num_dict = {}
for num in num_arr:
    num_dict[num] = 0

num_arr.sort()
def binary_search(arr, val):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return True
        elif arr[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return False

for val in num_cards:
    if binary_search(num_arr, val):
        num_dict[num] += 1
    else:
        continue

print(*num_dict.values())