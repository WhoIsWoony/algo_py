import sys
#sys.setrecursionlimit(10000)
#sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

### 정답체크용 ###
"""
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""
###############

#8
#2, 6 = 3 * 2
#6, 2 = 3 * 2
#2, 4, 2 
#2, 2, 4
#4, 2, 2
#2, 2, 2, 2

### 문제풀이용 ###

far_v, far = 0, 0
def solution(V, tree):
    #방문 초기화
    visited = [False for _ in range(V+1)]
    
    #start 정점으로 부터 가장 길이가 긴 정점을 찾는 DFS
    def dfs(start, distSum):
        global far_v, far
        visited[start]=True
        if far < distSum:
            far_v, far = start, distSum
        for child, dist in tree[start]:
             if not visited[child]:
                dfs(child, distSum + dist)
    
    #아무 임의이 정점으로부터 가장 거리가 먼 정점을 찾음
    dfs(1, 0)
    
    #방문 초기화
    visited = [False for _ in range(V+1)]

    #위에서 구한 가장 거리가 먼 정점으로부터 가장 거리가 먼 정점까지의 길이가 정답
    dfs(far_v, 0)
    return far
###############

### 입력, 결과 ###
V = int(input())
tree = [[] for _ in range(V+1)]
for i in range(V):
    info = list(map(int, input().split()))
    parent = info[0]
    for i in range(1, len(info)-1, 2):
        child = info[i]
        distance = info[i+1]
        tree[parent].append((child, distance))

#print(solution(N), checkAnswer(sol)) #체크용
print(solution(V, tree))          #풀이용
###############
