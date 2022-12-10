"""
### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""

### 환경세팅 ###
import sys                              
sys.stdin = open("./input.txt", "r")    #Tip1 : input.txt에 미리 입력을 복붙해놓으면 매번 복붙하는 것을 방지할 수 있다.
input = sys.stdin.readline              #Tip2 : 알고리즘용 빠른 읽기, 백준에서 유용
sys.setrecursionlimit(10**6)           #Tip3 : 파이썬 재귀함수 에러 방지, 백준에서 유용
INF = int(1e9)

### 문제풀이용 ###
from heapq import heappush, heappop
def solution(v,e,edges):
    parent = [0] * (v + 1)
    
    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    #cost를 기준으로 오름차순 정렬
    edges.sort()

    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    result = 0
    # 정렬된 간선을 하나씩 확인
    for edge in edges:
        cost, a, b = edge
        # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은것이므로  
        if find_parent(parent, a) != find_parent(parent, b):
            # 신장 트리에 간선 추가
            union_parent(parent, a, b)
            result += cost

    return result
        
### 입력 ###
v, e = map(int, input().split())
edges = []
for _ in range(e):
    v1, v2, w = map(int, input().split())
    edges.append((w, v1, v2))
print(solution(v,e,edges))
