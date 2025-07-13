from collections import deque

def bfs(start,G,N):
    dis = [-1] * (N+1)
    dis[start] = 0
    q = deque([start])
    while len(q) != 0:
        top = q.popleft()
        for v in G[top]:
            if dis[v] == -1:
                dis[v] = dis[top] + 1
                q.append(v)
    return max(dis)

def main():
    N1,N2,M = map(int,input().split())
    N = N1 + N2
    G = [list() for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)

    max1 = bfs(1,G,N)
    max2 = bfs(N,G,N)

    print(max1 + max2 + 1)

main()
# 深さ優先探索
# 木の最大の高さを求める

# 幅優先だった...