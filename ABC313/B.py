import sys
sys.setrecursionlimit(120000)

def main():
    def rec(pos):
        visited[pos] = True
        for v in L[pos]:
            if not visited[v]:
                rec(v)
        return

    N,M = map(int,input().split())
    L = [list() for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        L[a].append(b)
    # print(L)
    
    for pos in range(1,N+1):
        visited = [False] * (N+1)
        rec(pos)
        for v in visited[1:]:
            if not v:
                break
        else:
            print(pos)
            return
        
        visited = [False] * (N+1)
    print(-1)
    
main()
# 再帰