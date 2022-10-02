# 소수 판별 함수
from math import sqrt
def IsPrimeNumber(x):
    if x == 1: return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def TenToN(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 



def solution(n, k):
    transN = TenToN(n, k) + "0"
    print(transN)
    allN = []
    buf = ""
    for tn in transN:
        if tn == "0" and buf != "":
            print(buf)
            print(int(buf, k))
            print(IsPrimeNumber(int(buf)))
            if IsPrimeNumber(int(buf)):
                allN.append(buf) 
            buf=""
        elif tn != "0":
            buf+=tn
    
    return len(allN)

print(solution(437674,3))
print(solution(110011,10))