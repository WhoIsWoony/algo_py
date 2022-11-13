import sys
import math
#sys.setrecursionlimit(10000)
sys.stdin = open("./input.txt", "r")
#input = sys.stdin.readline

### 정답체크용 ###
"""
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""
###############


### 문제풀이용 ###
def solution(N):
    def isPrime(x):
        if x == 0 or x == 1: return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False 
        return True
    #2,3,5,7
    
    answer = []
    def dfs(x):
        if x > 10 ** (N-1):
            if isPrime(x):
                answer.append(x)
            return
        for n in range(1,10):
            num = x*10+n
            if isPrime(num):
                dfs(num)

    for n in [2,3,5,7]:
        dfs(n)
        
    for num in answer:
        print(num)
    
    

    return None
###############

### 입력, 결과 ###
N = int(input())

#print(solution(N), checkAnswer(sol)) #체크용
solution(N)                           #풀이용
###############
