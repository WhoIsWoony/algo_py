import sys
sys.stdin = open("./input.txt", "r")

### 정답체크용 ###
#answer = open("./output.txt", "r")
#def checkAnswer(sol):
#    return sol == answer.readline().strip()

### 문제풀이용 ###
def solution(N, L, gredient):
    global maxScore
    maxScore = 0

    def dfs(index, sumScore, sumKcal):
        global maxScore
        if sumKcal > L:
            return
        
        if maxScore < sumScore:
            maxScore = sumScore
        
        if index == N:
            return
        
        score, kcal = gredient[index]
        dfs(index+1, sumScore + score, sumKcal + kcal) #재료 사용시
        dfs(index+1, sumScore, sumKcal) #재료 미사용시
    
    dfs(0, 0, 0)

    return maxScore

### 입력, 결과 ###
for t in range(1, int(input())+1):
    answer = 0
    N, L = map(int, input().split())
    gredient = []
    for _ in range(N):
        score, kcal = map(int, input().split())
        gredient.append((score, kcal))
    
    sol = f"#{t} {solution(N, L, gredient)}"
    #print(sol, checkAnswer(sol))   #체크용
    print(sol)                      #풀이용
