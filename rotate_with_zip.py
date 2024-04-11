arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(arr)
# 1  2  3  4
# 5  6  7  8
# 9 10 11 12

print(list(map(list, zip(*arr))))
# zip(*arr)
# *는 zip 함수에 개별적으로 인자 전달
# 1 5 9
# 2 6 10
# 3 7 11
# 4 8 12

print(arr[::-1])
# 9 10 11 12
# 5  6  7  8
# 1  2  3  4

# 시계 방향 90 (= 반시계 270)
arr_90 = list(map(list, zip(*arr[::-1])))
print(arr_90)
# 9  5 1
# 10 6 2
# 11 7 3
# 12 8 4

arr_180 = [a[::-1] for a in arr[::-1]]
print(arr_180)
# 12 11 10 9
# 8  7  6  5
# 4  3  2  1

arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
# 4  8  12
# 3  7  11
# 2  6  10
# 1  5   9
