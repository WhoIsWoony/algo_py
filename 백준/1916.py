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
INF = int(1e9)
input = sys.stdin.readline              #Tip2 : 알고리즘용 빠른 읽기, 백준에서 유용
#sys.setrecursionlimit(10**6)           #Tip3 : 파이썬 재귀함수 에러 방지, 백준에서 유용

### 문제풀이용 ###
INF = int(1e9)
from heapq import heappush, heappop
def solution(n, m, a, b, graph):
    #초기세팅
    dist = [INF for _ in range(n)]
    dist[a] = 0

    # 시작 추가
    heap = []
    heappush(heap, (0, a))
    
    #다익스트라
    while heap:
        cost, node = heappop(heap)
        if dist[node] < cost:
            continue
        for nextCost, nextNode in graph[node]:
            nextCost += cost
            #이전까지cost+다음cost가 기존 다음노드의 최소경로보다 더 최소일때
            if nextCost < dist[nextNode]:
                dist[nextNode] = nextCost
                heappush(heap,(nextCost, nextNode))

    return dist[b]
        
### 입력 ###
n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
for _ in range(m):
    vs, vd, cost = map(int, input().split())
    graph[vs-1].append((cost, vd-1))
a, b = map(int, input().split())
print(solution(n, m, a-1, b-1, graph))
