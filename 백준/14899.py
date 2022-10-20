import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]
for r in range(n):
    graph[r] = list(map(int,input().split()))


def teamPower(team):
    sum = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            sum += (graph[team[i]][team[j]] + graph[team[j]][team[i]])
    return sum



MIN = 101
team1 = []
def dfs(start):
    global MIN
    if len(team1)==n/2:
        team2 = [x for x in range(n) if x not in team1]
        #print(team1, team2)
        #print(teamPower(team1), teamPower(team2))
        #print()
        if MIN > abs(teamPower(team1) - teamPower(team2)):
            MIN = abs(teamPower(team1) - teamPower(team2))
        return
    
    for i in range(start,int(n)):
        if i not in team1:
            team1.append(i)
            dfs(i+1)
            team1.pop()

dfs(0)

print(MIN)