def solution(lottos, win_nums):
    known = 0
    unknown = 0
    for my in lottos:
        if my == 0:
            unknown+=1
        elif my in win_nums:
            known+=1

    rank = [6, 6, 5, 4, 3, 2, 1]
    return [rank[known+unknown], rank[known]]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))