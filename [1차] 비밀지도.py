#오후 1시45분 시작
#오후 1시55분 종료

def solution(n, arr1, arr2):
    graph1 = []
    graph2 = []
    for i in range(n):
        row1 = format(arr1[i], 'b')
        while(len(row1)<n):
            row1 = "0" + row1
        row2 = format(arr2[i], 'b')
        while(len(row2)<n):
            row2 = "0" + row2
        graph1.append(row1)
        graph2.append(row2)

    answer = []
    for r in range(n):
        row = ""
        for c in range(n):
            if graph1[r][c] == "1" or graph2[r][c] == "1":
                row+="#"
            else:
                row+=" "
        answer.append(row)

    return answer

#print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))