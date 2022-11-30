### 문제풀이용 ###
def solution(topping):
    A={}
    B={}
    global cntA
    global cntB
    cntA, cntB = 0, 0
    def addToppping(who, toppi, setwho):
        global cntA, cntB
        if toppi in setwho:
            setwho[toppi] += 1
        else:
            if who == "B":
                cntB += 1
            else:
                cntA += 1
            setwho[toppi] = 1

    def deleteTopping(who, toppi, setwho):
        global cntA, cntB
        if toppi in setwho:
            setwho[toppi] -= 1
            if setwho[toppi] == 0:
                if who == "B":
                    cntB -= 1
                else:
                    cntA -= 1
    
    for toppi in topping:
        addToppping("B", toppi, B)
        
    answer = 0
    for toppi in topping:
        deleteTopping("B", toppi, B)
        addToppping("A",toppi, A)
        
        if cntA == cntB:
            answer += 1
    
    return answer
###############

### 입력, 결과 ###
print(solution([1, 2, 1, 3, 1, 4, 1, 2]	))
