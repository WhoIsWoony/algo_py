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
from copy import deepcopy
def solution(n, board):
    # UP
    def up(board):
        for j in range(n):
            pointer = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    # 포인터가 가리키는 수가 0일 때
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                    elif board[pointer][j]  == tmp:
                        board[pointer][j] *= 2
                        pointer += 1
                    # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                    else:
                        pointer += 1
                        board[pointer][j] = tmp
        return board

    # DOWN
    def down(board):
        for j in range(n):
            pointer = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j]  == tmp:
                        board[pointer][j] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp
        return board

    # LEFT
    def left(board):
        for i in range(n):
            pointer = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer]  == tmp:
                        board[i][pointer] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[i][pointer]= tmp
        return board

    # RIGHT
    def right(board):
        for i in range(n):
            pointer = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer]  == tmp:
                        board[i][pointer] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp
        return board

    # DFS
    def dfs(board, cnt):
        if cnt == 5:
            # 2차원 배열 요소 중 가장 큰 값 반환
            return max(map(max, board))

        # 상, 하, 좌, 우로 움직여 리턴한 값들 중 가장 큰 값 반환
        # board를 꼭 deepcopy하여 함수를 거친 board값이 다음 함수에 들어가지 못하도록 해주어야 한다.
        return max(dfs(up(deepcopy(board)), cnt + 1), dfs(down(deepcopy(board)), cnt + 1), dfs(left(deepcopy(board)), cnt + 1), dfs(right(deepcopy(board)), cnt + 1))
                

    return dfs(board, 0)
    

### 입력 ###
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
print(solution(n,board))
