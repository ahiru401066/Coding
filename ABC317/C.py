def main():
    def dfs(pos,count):
        nonlocal ans
        ans = max(ans,count)
        visited[pos] = True
        for v,c in G[pos]:
            if visited[v] != True:
                dfs(v, count+c)
                
        visited[pos] = False
        return

    N,M = map(int,input().split())
    G = [list() for _ in range(N+1)]
    for _ in range(M):
        a,b,c = map(int,input().split())
        G[a].append([b,c])
        G[b].append([a,c])

    ans = 0
    visited = [False] * (N+1)
    for pos in range(1,N+1):
        dfs(pos,0)
    
    print(ans)
    

main()
# 最短経路問題(スタート任意)

# データ受け取り
# ロジック解決
# 実装