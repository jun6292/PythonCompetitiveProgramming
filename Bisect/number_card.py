# https://www.acmicpc.net/problem/10815
# 숫자 카드

N = int(input())
num_cards = list(map(int, input().split()))
M = int(input())
num_arr = list(map(int, input().split()))
num_cards.sort()
answer = []

def binary_search(num_cards, val):
    left, right = 0, len(num_cards) - 1
    while left <= right:
        mid = (left + right) // 2
        if num_cards[mid] == val:
            return True
        elif num_cards[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return False

for num in num_arr:
    if binary_search(num_cards, num):
        answer.append(1)
    else:
        answer.append(0)

print(*answer)