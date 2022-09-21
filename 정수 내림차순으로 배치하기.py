def solution(n):
    nList = []
    while n > 0:
        nList.append(n % 10)
        n = int(n/10)
    nList.sort(reverse=True)

    answer = 0
    digit = 10 ** (len(nList)-1)
    for i in range(0, len(nList)):
        answer += (nList[i]*digit)
        digit /= 10
            
    return int(answer)

print(solution(118372))