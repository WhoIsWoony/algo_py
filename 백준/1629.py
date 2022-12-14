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
def solution(n, graph):

    #3 2
    #1 3
    #2 3

    #4 4
    #1 2
    #2 3
    #3 4
    #4 2

    
    v = [False for _ in range(n)]
    
    def bfs(s):
        q = deque()
        q.append(s)
        while q:
            c = q.popleft()
            v[c] = True
            for nx in graph[c]:
                if not v[nx]:
                    q.append(nx)
    cnt = 0
    for s in range(n):
        if not v[s]:
            cnt+=1
            if cnt == 2:
                return "YES"
            bfs(s)

    return "NO"
        

### 입력 ###
t = int(input())
for _ in range(t):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1-1].append(v2-1)
        graph[v2-1].append(v1-1)
    print(solution(n, graph))
    
    
