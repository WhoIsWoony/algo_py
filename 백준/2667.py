import sys
#sys.setrecursionlimit(10000)
sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline


"""
### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""
### 문제풀이용 ###
from collections import deque
def solution(n, houses):
    def bfs(sr,sc):
        count = 0
        q = deque()
        houses[sr][sc] = -1 #방문했음
        q.append((sr, sc))
        while q:
            cr, cc= q.popleft()
            count += 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr and nr < n and 0 <= nc and nc < n and houses[nr][nc] == 1:
                    houses[nr][nc] = -1 #방문했음
                    q.append((nr, nc))
        return count
    
    answer = []
    area = 0
    for r in range(n):
        for c in range(n):
            if houses[r][c] == 1:
                count = bfs(r,c)
                answer.append(count)
                area += 1
    answer.sort()

    print(area)
    for nHouse in answer:
        print(nHouse)

    return answer

### 입력 ###
n = int(input())
houses = [list(map(int, list(input().strip()))) for _ in range(n)]

### 출력 ###
#print(solution(N), checkAnswer(sol)) #체크용
solution(n, houses)                        #풀이용
