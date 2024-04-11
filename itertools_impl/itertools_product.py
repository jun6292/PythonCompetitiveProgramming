# 중복순열
# 순서 O, 중복 O
arr = [1, 2, 3, 4]


def product(n, new_arr):
    if n == len(new_arr):
        print(new_arr)
        return

    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])


product(2, [])