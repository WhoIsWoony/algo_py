def rotate(graph, y1, x1, y2, x2):
    xMin = min(x1-1, x2-1)
    yMin = min(y1-1, y2-1)
    xMax = max(x1-1, x2-1)
    yMax = max(y1-1, y2-1)

    MIN = 1e4+1

    t = graph[yMin][xMin]
    for y in range(yMin, yMax, 1):
        graph[y][xMin] = graph[y+1][xMin]
        if graph[y][xMin] < MIN:
            MIN = graph[y][xMin]

    for x in range(xMin, xMax, 1):
        graph[yMax][x] = graph[yMax][x+1]
        if graph[yMax][x] < MIN:
            MIN = graph[yMax][x]

    for y in range(yMax, yMin, -1):
        graph[y][xMax] = graph[y-1][xMax]
        if graph[y][xMax] < MIN:
            MIN = graph[y][xMax]

    for x in range(xMax, xMin+1, -1):
        graph[yMin][x] = graph[yMin][x - 1]
        if graph[yMin][x] < MIN:
            MIN = graph[yMin][x]

    graph[yMin][xMin+1] = t
    if graph[yMin][xMin+1] < MIN:
        MIN = graph[yMin][xMin+1]
    
    return MIN


def solution(rows, columns, queries):
    answer = []

    v = 1
    graph = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(v)
            v+=1
        graph.append(row)

    for q in queries:
        answer.append(rotate(graph, q[0],q[1],q[2],q[3]))

    return answer
    
#print(solution(6,6,[[2,2,5,4]]))
#print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
#print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
#print(solution(1000,97,[[1,1,100,97]]))