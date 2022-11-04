from collections import deque
import sys
sys.stdin = open("./input.txt", "r")
#input = sys.stdin.readline

### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
###############


### 문제풀이용 ###
def solution(graph, R, C):
    def program(r, c):
        queue = deque()
        queue.append((r,c))
        graph[r][c] = 0
        while(queue):
            current_r, current_c = queue.pop()
            #Right
            if(current_r < R - 1 and graph[current_r+1][current_c]==1):
                queue.append((current_r+1, current_c))
                graph[current_r+1][current_c] = 0
            #Down
            if(current_c < C - 1 and graph[current_r][current_c+1]==1):
                queue.append((current_r, current_c+1))
                graph[current_r][current_c+1] = 0
            #Left
            if(current_c > 0 and graph[current_r][current_c-1]==1):
                queue.append((current_r, current_c-1))
                graph[current_r][current_c-1] = 0
            #Up
            if(current_r > 0 and graph[current_r-1][current_c]==1):
                queue.append((current_r-1, current_c))
                graph[current_r-1][current_c] = 0
    answer = 0
    for r in range(R):
        for c in range(C):
            if(graph[r][c]==1):
                program(r, c)
                answer = answer + 1
                
    return answer
###############

### 입력, 결과 ###
N = input()
A,B,C,D,E,F = map(int, input().split())
    
sol = solution(N,A,B,C,D,E,F)
#print(sol, checkAnswer(sol))   #체크용
print(sol)                      #풀이용
###############
