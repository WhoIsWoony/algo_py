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
sys.setrecursionlimit(10**6)            #Tip3 : 파이썬 재귀함수 에러 방지, 백준에서 유용
INF = int(1e9)

### 문제풀이용 ###
from heapq import heappush, heappop
def dijkstra(start, graph, n):
    dist = [float("inf") for _ in range(n)]
    q = []
    heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        cost, current = heappop(q)
        for costNext, currentNext in graph[current]:
            costNext += cost
            if dist[currentNext] > costNext:
                dist[currentNext] = costNext
                heappush(q, (costNext, currentNext))
    return dist

def solution(graph, n, m, k, x):
    dist = dijkstra(x, graph, n)
    answer = ""
    for i in range(len(dist)):
        if dist[i] == k:
            answer += (str(i+1)+"\n")
    if answer == "": return -1
    else: return answer[:-1]

### 입력 ###
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    v1, v2= map(int, input().split())
    graph[v1-1].append((1, v2-1))
print(solution(graph, n, m, k, x-1))