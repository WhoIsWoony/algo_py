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
import itertools
def solution(n,words):
    asciiDigitSum = {}
    for word in words:
        for i in range(0, len(word)):
            digit = (10 ** (len(word) - i - 1))
            if word[i] in asciiDigitSum:
                asciiDigitSum[word[i]] += digit
            else:
                asciiDigitSum[word[i]] = digit
        
    digits = []
    for key in asciiDigitSum.keys():
        digits.append(asciiDigitSum[key])
    digits.sort(reverse=True)
    
    i = 9
    answer = 0;
    for digit in digits:
        answer += (digit * i)
        i -= 1

    return answer
    

### 입력 ###
n = int(input())
words = [list(input().strip()) for _ in range(n)]
print(solution(n,words))
