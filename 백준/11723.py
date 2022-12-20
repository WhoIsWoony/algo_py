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
sys.setrecursionlimit(10**6)            #Tip3 : 파이썬 재귀함수 에러 방지, 백준에서 유용
INF = int(1e9)
    
### 문제풀이용 ###
global num
def solution(cmd, item):
    global num


### 입력 ###
import sys                              
input = sys.stdin.readline              #Tip2 : 알고리즘용 빠른 읽기, 백준에서 유용
bit = 0

m = int(input())
for _ in range(m):
    cmd = input().split()

    if cmd[0] == "all":
        bit = (1<<20) - 1
    elif cmd[0] == "empty":
        bit = 0
    else:
        op, n = cmd[0], 1 << (int(cmd[1]) - 1)
        if op == "add":
            bit = bit | n
        elif op == "remove":
            bit = bit & ~n
        elif op == "check":
            print(1 if bit & n else 0)
        elif op == "toggle":
            bit = bit ^ n