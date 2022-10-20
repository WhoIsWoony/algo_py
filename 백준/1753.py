import sys
import heapq  # 우선순위 큐 구현을 위함
fastread = sys.stdin.readline

def dijkstra(graph, start):
    dist = [float('inf') for _ in range(len(graph))]
    dist[start] = 0

    heap = []
    heapq.heappush(heap,(0, start))

    while heap:
        curDist, curNode= heapq.heappop(heap)
        if dist[curNode] < curDist:
            continue
            
        for toDist, toNode in graph[curNode]:
            d = toDist + curDist
            if dist[toNode] > d:
                dist[toNode] = d
                heapq.heappush(heap, (d, toNode))
    return dist

#Input = N
V, E = map(int,fastread().split())
vs = int(fastread())-1

graph = [[] for _ in range(V)]
for e in range(E):
    u,v,w = map(int,fastread().split())
    graph[u-1].append((w, v-1))

result = dijkstra(graph, vs)
for i in result:
    print(i if i != float('inf') else "INF")