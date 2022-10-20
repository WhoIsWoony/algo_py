import sys
input = sys.stdin.readline

N = int(input())
graph = [[0] * N for _ in range(N)]

def checkChess(graph, queenY, queenX):
    #좌표로부터 좌 하향대각선 체크
    qvy, qvx = queenY, queenX
    while qvy > 0 and qvx > 0:
        qvy-=1
        qvx-=1
        if graph[qvy][qvx] == 1:
            return False
        
    #좌표로부터 우 상향대각선 체크
    qvy, qvx = queenY, queenX
    while qvy > 0 and qvx < N-1:
        qvy-=1
        qvx+=1
        if graph[qvy][qvx] == 1:
            return False
    
    return True

answer=0
checkX = [0 for _ in range(N)]
def dfs(y):
    global answer
    if y == N:
        answer += 1
        return
    for x in range(N):
        if checkX[x] == 1:
            continue
        if checkChess(graph, y, x):
            graph[y][x] = 1
            checkX[x] = 1
            dfs(y+1)
            checkX[x] = 0
            graph[y][x] = 0

dfs(0)

print(answer)