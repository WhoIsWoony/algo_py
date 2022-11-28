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
#sys.setrecursionlimit(10**6)           #Tip3 : 파이썬 재귀함수 에러 방지, 백준에서 유용

### 문제풀이용 ###
import heapq
INF = float("inf")
def solution(n,m,x,graph):
    def dijkstra(start):
        distance = [INF] * (n)
        q = []
        heapq.heappush(q, (0, start))  # 시작노드 정보 우선순위 큐에 삽입
        distance[start] = 0            # 시작노드->시작노드 거리 기록
        while q:
            d, town = heapq.heappop(q)
            # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
            if distance[town] < d:
                continue
            # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
            for nd, nTown in graph[town]:
                cost = distance[town] + nd   # 시작->node거리 + node->node의인접노드 거리
                if cost < distance[nTown]:      # cost < 시작->node의인접노드 거리
                    distance[nTown] = cost
                    heapq.heappush(q, (cost, nTown))
        return distance

    
    goHome = dijkstra(x)
    for student in range(0, n):
        goParty = dijkstra(student)
        goHome[student] += goParty[x]
    return max(goHome)
    

### 입력 ###
n, m, x = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    town1, town2, t = map(int, input().split())
    graph[town1-1].append((t, town2-1))
print(solution(n,m,x-1,graph))
