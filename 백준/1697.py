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
def solution(N, K):
    q = deque()
    q.append(N)

    MAX = 10 ** 5
    dist = [0] * (MAX + 1)
    
    while q:
        x = q.popleft()
        if x == K:
            answer = dist[x]
            break

        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)
        
    return answer

### 입력 ###
N, K = map(int,input().split())

### 출력 ###
#print(solution(N), checkAnswer(sol)) #체크용
print(solution(N, K))                        #풀이용
