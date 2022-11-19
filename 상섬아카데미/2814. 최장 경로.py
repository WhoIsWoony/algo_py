import sys
sys.stdin = open("./input.txt", "r")

### 정답체크용 ###
#answer = open("./output.txt", "r")
#def checkAnswer(sol):
#    return sol == answer.readline().strip()

### 문제풀이용 ###

def solution(N, M, graph):
    global far_v, far
    far_v, far = 0, 0

    visited = [False for _ in range(N)]
    def dfs(now, distance):
        global far_v, far
        visited[now] = True
        if far < distance:
            far_v, far = now, distance

        for next in graph[now]:
            if not visited[next]:
                dfs(next, distance + 1)
                visited[next]=False
    
    dfs(0, 1)
    
    visited = [False for _ in range(N)]
    dfs(far_v, 1)
    
    return far

### 입력, 결과 ###
for t in range(1, int(input())+1):
    answer = 0
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start-1].append(end-1)
        graph[end-1].append(start-1)
    
    sol = f"#{t} {solution(N, M, graph)}"
    #print(sol, checkAnswer(sol))   #체크용
    print(sol)                      #풀이용
