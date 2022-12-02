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
def solution(command):
    commandSplit = command.split("-")
    for i in range(len(commandSplit)):
        commandSplit[i] = commandSplit[i].split("+")
    
    for i in range(len(commandSplit)):
        value = 0
        for j in range(len(commandSplit[i])):
            value += int(commandSplit[i][j])
        commandSplit[i] = value
    
    answer = commandSplit[0]
    for i in range(1, len(commandSplit)):
        answer -= commandSplit[i]
    
    return answer

### 입력 ###
command = input().rstrip()
print(solution(command))
