"""
### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""
import sys
sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

### 문제풀이용 ###
def solution(commands, size, arr):
    nD = commands.count("D")
    if nD > size:
        return "error"
    elif nD == size or size == 0:
        return "[]"
    
    commands = commands.replace("RR","")
    nD,nB,nR = 0,0,0
    flag = True
    for command in commands:
        if command == "R":
            flag = not flag
            nR += 1
        else:
            if flag:
                nD += 1
            else:
                nB += 1
    arr = arr[nD:size-nB]
    #배열 뒤집기
    if nR % 2 == 1:
        arr = arr[::-1]
    return "["+",".join(arr)+"]"

### 입력 ###
T = int(input())
for t in range(T):
    commands = input().rstrip()
    size = int(input())
    arr = input().rstrip()[1:-1].split(",")
    print(solution(commands, size, arr))
