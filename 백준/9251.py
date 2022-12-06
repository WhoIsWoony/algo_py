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
def solution(word1, word2):
    h, w = len(word1), len(word2)
    cache = [[0] * (w+1) for _ in range(h+1)]

    for i in range(1, h+1):
        for j in range(1, w+1):
            if word1[i-1] == word2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j] = max(cache[i][j-1], cache[i-1][j])
    return cache[-1][-1]
    
        
### 입력 ###

word1, word2 = input().strip(), input().strip()
print(solution(word1, word2))
