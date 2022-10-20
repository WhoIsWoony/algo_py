import sys
input = sys.stdin.readline

n = int(input())
arrA = list(map(int, input().split()))
opA = list(map(int, input().split()))

def div(x1, x2): 
    return x1//x2 if x1 > 0 else -(-x1//x2)

maxResult = int(-1e10)
minResult = int(1e10)

def dfs(sum, a):
    global maxResult
    global minResult
    if a == len(arrA):
        if maxResult < sum:
            maxResult = sum
        if minResult > sum:
            minResult = sum

    for i in range(len(opA)):
        if opA[i] <= 0:
            continue

        nSum = 0
        if(i==0): nSum = sum + arrA[a]
        elif(i==1): nSum = sum - arrA[a]
        elif(i==2): nSum = sum * arrA[a]
        elif(i==3): nSum = div(sum, arrA[a])

        opA[i] -= 1
        dfs(nSum, a+1)
        opA[i] += 1
            
dfs(arrA[0],1)

print(maxResult)
print(minResult)