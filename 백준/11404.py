import sys
fastread = sys.stdin.readline

def floyd(dist):
    for k in range(0, n):
        for a in range(0, n):
            for b in range(0, n):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
    return dist

n = int(fastread())                    #도시수
m = int(fastread())                    #버스수

dist = [[float('inf')] * n for _ in range(n)]
for a in range(0, n):
    for b in range(0, n):
        if a == b:
            dist[a][b] = 0

for _ in range(m):
    a, b, c = map(int, fastread().split())  #버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c
    if dist[a-1][b-1] > c:                  #!!!시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
        dist[a-1][b-1] = c

result = floyd(dist)

for a in range(0, n):
  for b in range(0, n):
    if dist[a][b] == float('inf'):      # if not reachable, print 0
      print(0, end = " ")
    else:                               # if reachable, print the distance
      print(result[a][b], end = " ")
  print()