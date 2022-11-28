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
def solution(n, place):
    waters = set([])
    for h in place:
        waters.update(h)
    

    v = None
    def bfs(sr, sc, water):
        q = deque()
        q.append((sr, sc))
        v[sr][sc] = True
        while q:
            cr, cc = q.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = cr + dr, cc + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                if not v[nr][nc] and place[nr][nc] > water:
                    q.append((nr, nc))
                    v[nr][nc] = True

    answer = 1
    for water in waters:
        v = [[False] * n for _ in range(n)]
        count = 0
        for r in range(n):
            for c in range(n):
                if not v[r][c] and place[r][c] > water:
                    bfs(r,c,water)
                    count += 1
        answer = max(answer, count)
    return answer    

### 입력 ###
n = int(input())
place = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, place))
