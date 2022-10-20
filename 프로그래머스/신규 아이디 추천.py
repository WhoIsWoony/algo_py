#최소 2가지 이상 단품 메뉴로 코스 구성
#최소 2명 이상의 손님으로 부터 주문된 단품메뉴 조합에 대해서 후보로 포함
def combination(case, arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen):
        if len(chosen) == r:
            if "".join(chosen) in case:
                case["".join(chosen)] += 1
            else:
                case["".join(chosen)] = 1
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])

def solution(orders, courses):
    answer = []
    case={}
    for order in orders:
        for course in courses:
            combination(case, list(order), course)
    
    maxInCourse={}
    for k, v in case.items():
        if v >= 2 and len(k) in courses:
            if len(k) in maxInCourse:
                maxInCourse[len(k)] = max(maxInCourse[len(k)], v)
            else:
                maxInCourse[len(k)] = v
    print(maxInCourse)
    for k, v in case.items():
        if v >= 2 and len(k) in maxInCourse:
            if maxInCourse[len(k)] == v:
                answer.append(k)
    answer.sort()
    
    """
    for k, v in case.items():
        print(k,v)
    print()
    """
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))