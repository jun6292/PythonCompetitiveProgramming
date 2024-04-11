from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))

print(result)

# from itertools_impl import combinations
#
# data = ['A', 'B', 'C']
# result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
#
# print(result)
#
# from itertools_impl import product
#
# data = ['A', 'B', 'C']
# result = list(product(data, repeat=2)) # 2개를 뽑는 모든 조합 구하기
#
# print(result)
#
# from itertools_impl import combinations_with_replacement
#
# data = ['A', 'B', 'C']
# result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
#
# print(result)