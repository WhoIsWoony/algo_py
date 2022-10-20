#DP Memoey 저장소
dp = [0,1]

#TestCase Number = T
T = int(input())
#TestCase Procedure = t
for t in range(0,T):
    #Input = N
    N = int(input())

    #fibonacci의 결과를 DP에 저장
    for n in range(len(dp),N):
        dp.append(dp[n-1] + dp[n-2])

    #결과 출력
    if N==0:
        print(1, 0)
    elif N==1:
        print(0, 1)
    else:
        print(dp[N-1],dp[N-2]+dp[N-1])