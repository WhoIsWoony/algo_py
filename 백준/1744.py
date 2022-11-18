import sys
sys.setrecursionlimit(10000)
sys.stdin = open("./input.txt", "r")
#input = sys.stdin.readline
from queue import PriorityQueue


"""
### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""

### 문제풀이용 ###
def solution(N, arr):
    positive = PriorityQueue()
    negative = PriorityQueue()
    one = 0
    zero = 0
    for n in arr:
        if n == 0:
            zero += 1
        elif n == 1:
            one += 1
        elif n >= 2:
            positive.put(-n) 
        else:
            negative.put(n) 

    answer = one
    while positive.qsize() > 1:
        answer += (-positive.get() * -positive.get())
    while negative.qsize() > 1:
        answer += (negative.get() * negative.get())
    
    while positive.qsize() > 0:
        answer += (-positive.get())
    
    if(zero == 0):
        while negative.qsize() > 0:
            answer += negative.get()

    return answer

### 입력 ###
N = int(input())
arr = [int(input()) for _ in range(N)]

### 출력 ###
#print(solution(N), checkAnswer(sol)) #체크용
print(solution(N, arr))                        #풀이용
