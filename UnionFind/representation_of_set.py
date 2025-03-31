# 백준 1717 집합의 표현
# https://www.acmicpc.net/problem/1717

# 유니온 파인드 1717번 문제 풀다가 런타임 에러(Recursion Error) 계속 뜨길래 공유합니다
# RecursionError는 재귀와 관련된 에러고 Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때 발생한다고 합니다
# 백준 채점 서버에서 recursionlimit 값이 1000이라서
# sys.setrecursionlimit(숫자)로 재귀 뎁스 늘리거나
# 재귀 쓰지말고 반복문으로 푸세용

# 유니온 파인드 문제
# 0 입력 시 두 노드를 연결
# 1 입력 시 두 노드가 연결되었는지 확인하여 결과를 출력

import sys
sys.setrecursionlimit(10 ** 6)


n, m = map(int, input().split())

parent = [i for i in range(n + 1)]  # 노드들의 부모 정보, 각각의 부모는 자기 자신으로 초기화

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    parent[parent_a] = parent_b

for _ in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:  # 합집합 연산
        union(a, b)
    else:  # 두 원소가 같은 집합에 포함되어 있는지 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
