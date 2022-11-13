import sys
sys.setrecursionlimit(10000)
#sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

### 정답체크용 ###
"""
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""
###############


### 문제풀이용 ###
def solution(N, M, graph):
    answer = 0
    visited = [False for _ in range(N+1)]
    def dfs(start):
        visited[start] = True
        for to in graph[start]:
            if not visited[to]:
                dfs(to)
    
    for i in range(1, N+1):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer
###############

### 입력, 결과 ###
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#print(solution(N), checkAnswer(sol))   #체크용
print(solution(N, M, graph))               #풀이용
###############
