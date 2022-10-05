def checkRight(room):
    for r in range(len(room)):
        for c in range(len(room[r])):
            if room[r][c] == "P":
                for rr in range(1,3):
                   if c+rr > 4: break
                   if room[r][c+rr] == "P":
                        return False
                   elif room[r][c+rr] == "X":
                        break
                for d in range(1,3):
                   if r+d > 4: break
                   if room[r+d][c] == "P":
                        return False
                   elif room[r+d][c] == "X":
                        break
                if 0 < r < 4 and 0 < c < 4:
                    if room[r+1][c+1] == "P" and (room[r][c+1] == "O" or room[r+1][c] == "O"):
                       return False
                    if room[r+1][c-1] == "P" and (room[r][c-1] == "O" or room[r+1][c] == "O"):
                       return False
    return True

def solution(places):
    answer = []
    for room in places:
       print(checkRight(room))
            
    return answer

print(solution([["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]]))