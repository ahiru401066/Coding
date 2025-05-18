# 深さ優先探索の基礎
import sys
sys.setrecursionlimit(120000)

def main():
    def dfs(pos, G, visited):
        visited[pos] = True
        for i in G[pos]:
            if visited[i] == False:
                dfs(i,G,visited)
    
    n,m = map(int,input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    G = [list() for _ in range(n+1)]
    for a,b in edges:
        G[a].append(b)
        G[b].append(a)

    visited = [False] * (n+1) #探索チェック
    dfs(1, G, visited)


    answer = True
    for i in range(1,n+1):
        if visited[i] == False:
            answer = False
            break
    
    if answer == True: print("The graph is connected.")
    else: print("The graph is not connected.")

main()