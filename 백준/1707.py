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
from collections import deque
def solution(V,E,graph):
    global v
    v = [0 for _ in range(V)]
    
    def bfs(start):
        global v
        q = deque()
        q.append(start)
        v[start] = 1
        while q:
            c = q.popleft()
            for n in graph[c]:
                if v[n] == 0:
                    v[n] = -v[c]
                    q.append(n)
                elif v[n] == v[c]:
                    return False
        return True

    for start in range(V):
        if v[start] == 0:
            result = bfs(start)
            if not result:
                return "NO"
    return 'YES'
    
        

### 입력 ###
T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1-1].append(v2-1)
        graph[v2-1].append(v1-1)

    print(solution(V,E,graph))
