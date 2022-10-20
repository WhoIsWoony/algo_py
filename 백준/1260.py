from collections import deque
from copy import copy
from queue import Queue
import sys
fastread = sys.stdin.readline

n,m,start = map(int, fastread().split(" "))

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, fastread().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for row in graph:
    row.sort()

def DFS(graph, now, visited):
    print(now, end=' ')
    visited[now] = True
    for to in graph[now]:
        if not visited[to]:
            DFS(graph, to, visited)
    
visited = [False for _ in range(n+1)]
DFS(graph, start, visited)

print()

def BFS(graph, now, visited):
    queue = deque([now])
    visited[now] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False for _ in range(n+1)]
BFS(graph, start, visited)