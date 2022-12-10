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

def solution(n):
    #첫패턴 3번
    #두패턴 1번하고 skip하고 1번
    #세패턴 3번
    pattern = [
        "***",
        "* *",
        "***",
    ]


    p = 3
    while p != n:
        p *= 3

        newPattern = ["" for _ in range(p)]
        #27이면 패턴은 9짜리 패턴 복사, 0~9번째 줄 패턴복사
        for row in range(p//3):
            newPattern[row] = pattern[row] * 3

        #중간 공백 포함하여 복사, 9패턴 + 9공백 + 9패턴
        for row in range(p//3):
            newPattern[row+(p//3)] = pattern[row] * 1
            newPattern[row+(p//3)] += (" " *(p//3))
            newPattern[row+(p//3)] += pattern[row] * 1

        #중간 공백 포함하여 복사, 9패턴 + 9공백 + 9패턴복사
        for row in range(p//3):
            newPattern[row+(p//3*2)] = pattern[row] * 3

        pattern = newPattern
    

    for row in pattern:
        print(row)
    
        
### 입력 ###
n = int(input())
solution(n)
