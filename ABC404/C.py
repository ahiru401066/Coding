def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    pos=1; count=0
    ans = None
    ans = dfs(1,count,graph,n)
    if ans: print("Yes")
    else: print("No")

def dfs(pos,count,graph,n):
    if pos == 1 and count == n:
        return True
    if count == n: return None
    for i in graph[pos]:
        dfs(i,count+1,graph,n)

main()

"""
無向グラフは辺の出発と到着が等しい、、、
深さ優先探索を行い視点に戻る、かつ頂点を全て通っているかどうか？
"""