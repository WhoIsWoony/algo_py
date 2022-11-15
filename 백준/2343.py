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
def solution(N, M, lectures):
    #left = 최소 블루레이 크기, right = 최대 블루레이 크기
    left = 0
    right = 0
    for i in lectures:
        if left < i:
            left = i
        right += i

    while left <= right:
        middle = int((left + right) / 2)
        sum = 0
        count = 0
        for length in lectures:
            if sum + length > middle:
                count += 1
                sum = 0
            sum += length
        if sum != 0:
            count += 1

        if count > M:
            left = middle + 1
        else:
            right = middle - 1
    return left

### 입력 ###
N, M = map(int,input().split())
lectures = list(map(int, input().split()))

### 출력 ###
#print(solution(N), checkAnswer(sol)) #체크용
print(solution(N, M, lectures))                        #풀이용
