import sys
sys.stdin = open("./input.txt", "r")
#input = sys.stdin.readline

### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
###############


### 문제풀이용 ###
def solution(N,A,B,C,D,E,F):
    if N == 1:
        return A+B+C+D+E+F - max(A,B,C,D,E,F)

    sum = 0
    nDice = N*N*5


    #위 끝 모서리 3개면 노출, 4개
    minAF = min(A, F)
    up3 = min(
        minAF+B+C,
        minAF+C+E,  
        minAF+D+B, 
        minAF+E+D, 
    )
    sum += (up3*4)
    nDice -= (4*3)

    #아래 끝 모서리 2개면 노출, 4개
    down2 = min(
        minAF+B,
        minAF+C,
        minAF+D,
        minAF+E,
        B+D,
        C+B,
        D+E,
        E+C,
    )
    sum += (down2*4)
    nDice -= (4*2)

    
    #아래 제외 전체 모서리 2개면 노출, N - 양쪽모서리 * 아래제외 모서리수
    sum += (down2 * ((N - 2) * 8))
    nDice -= ((N - 2) * 8 * 2)

    #아래 모서리 포함 1개면만 노출
    sum += (nDice * min(A,B,C,D,E,F))
                
    return sum
###############

### 입력, 결과 ###
N = int(input())
A,B,C,D,E,F = map(int, input().split())
    
sol = solution(N,A,B,C,D,E,F)
#print(sol, checkAnswer(sol))   #체크용
print(sol)                      #풀이용
###############
