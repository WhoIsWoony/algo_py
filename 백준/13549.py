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
sys.setrecursionlimit(10**6)           #Tip3 : 파이썬 재귀함수 에러 방지, 백준에서 유용
INF = int(1e9)

### 문제풀이용 ###
from collections import deque
def solution(a, b):
    visited = [-1 for _ in range(100001)]
    q = deque()
    visited[a]=0
    q.append(a)
    while q:
        c = q.popleft()
        if c == b:
            return visited[b]

        if 0 <= c-1 < 100001 and visited[c-1] == -1:
            visited[c-1] = visited[c] + 1
            q.append(c-1)
        
        if 0 < c*2 < 100001 and visited[c*2] == -1:
            visited[c*2] = visited[c]
            q.appendleft(c*2)
        
        if 0 <= c+1 < 100001 and visited[c+1] == -1:
            visited[c+1] = visited[c] + 1
            q.append(c+1)
        
### 입력 ###
a, b = map(int, input().split())
print(solution(a, b))
