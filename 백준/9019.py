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
    visit = [False for _ in range(10000)]   
    q = deque()
    q.append((a, ""))
    while q:
        n, path = q.popleft()
        if n == b: return path

        commands={
            "D": (2*n)%10000,
            "S": (n-1)%10000,
            "L": (10*n+(n//1000))%10000,
            "R": (n//10+(n%10)*1000)%10000
        }
        
        for comm, value in commands.items():
            if not visit[value]:
                visit[value] = True
                q.append((value, path + comm))
            

### 입력 ###

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    print(solution(a, b))
