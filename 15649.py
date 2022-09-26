import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split(" "))

inBox = list(range(1,N+1))

def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(" ".join(map(str, chosen)))
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)

permutation(inBox, M)