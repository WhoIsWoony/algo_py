from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(map(int,list(input()[:-1]))))

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque([[0,0]])
while queue:
    r, c = queue.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0<= nc < C and graph[nr][nc] == 1:
            queue.append([nr, nc])
            graph[nr][nc] = graph[r][c] + 1

print(graph[R-1][C-1])