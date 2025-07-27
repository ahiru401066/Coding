import sys
sys.setrecursionlimit(120000)

def main():
    def dfs(pos,li):
        visited[pos] = True
        if len(li) == N:
            L.append(li)

        for v in range(N):
            if not visited[v]:
                dfs(v,li+[S[v]])
        visited[pos] = False
        return
        
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    L = []

    visited = [False] * (N)
    for pos in range(N):
        dfs(pos,[S[pos]])

    # print(L)
    for l in L:
        for i in range(len(l)-1):
            count = 0
            for k in range(M):
                if l[i][k] != l[i+1][k]: count += 1
            if count != 1:
                break
        else:
            print("Yes")
            return
    print("No")

main()
# 全探索