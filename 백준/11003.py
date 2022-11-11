from collections import deque
import sys
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
def solution(N, L, arr):
    answer = []
    queue = deque()
    for i in range(0, N):
        while queue and queue[-1][1] > arr[i]:
            queue.pop()
        while queue and queue[0][0] < i-L+1:
            queue.popleft()
        queue.append((i, arr[i]))
        print(queue[0][1], end=" ")
    return answer;
###############

### 입력, 결과 ###
N, L = map(int,input().split())
arr = list(map(int,input().split()))
#print(solution(N), checkAnswer(sol))   #체크용
solution(N, L, arr)               #풀이용
###############
