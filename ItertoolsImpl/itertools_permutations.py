# ItertoolsImpl 없이 순열 구현
# 순서 O, 중복 X
# visited 배열 존재 -> 순서 고려
# parameter: 뽑을 개수, 뽑힌 값을 담는 배열
arr = [1, 2, 3, 4]
visited = [False] * len(arr)


def permutations(n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutations(n, new_arr + [arr[i]])
            visited[i] = False


permutations(2, [])
