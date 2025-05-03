import sys
sys.setrecursionlimit(10**7)

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    if m != n:
        print("No")
        return
    
    for i in range(1, n+1):
        if len(graph[i]) != 2:
            print("No")
            return
    
    visited = [False] * (n+1)
    def dfs(v):
        visited[v] = True
        for nv in graph[v]:
            if not visited[nv]:
                dfs(nv)

    dfs(1)

    if all(visited[1:]):
        print("Yes")
    else:
        print("No")

main()