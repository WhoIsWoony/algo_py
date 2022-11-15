import sys
#sys.setrecursionlimit(10000)
sys.stdin = open("./input.txt", "r")
#input = sys.stdin.readline

"""
### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""

### 문제풀이용 ###
def solution(A, X):
    for x in X:
        if x in A:
            print(1)
        else:
            print(0)
    return 

### 입력 ###
N = int(input())
A = {}
for a in map(int, input().split()):
    A[a] = True

M = int(input())
X = list(map(int, input().split()))

### 출력 ###
#print(solution(N), checkAnswer(sol)) #체크용
solution(A, X)                        #풀이용
