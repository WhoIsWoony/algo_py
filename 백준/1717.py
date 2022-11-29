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
#import copy

### 문제풀이용 ###
def solution(n, commands):
    dp = [i for i in range(n+1)]
    
    def find(x):
        if dp[x] == x:
            return x
        else:
            parent = find(dp[x])
            dp[x] = parent
            return parent
    
    def union(x, y):
        x = find(x)
        y = find(y)
        dp[y] = x
    
    for command in commands:
        c, a, b = command[0], command[1], command[2]
        if c == 0:
            union(a, b)
        elif c == 1:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
            

### 입력 ###
n, m = map(int,input().split())
commands = [list(map(int,input().split())) for _ in range(m)]
solution(n,commands)
