from collections import deque

def main():
    n,m = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(m)]
    G = [list() for _ in range(n+1)]
    for a,b in edges:
        G[a].append(b)
        G[b].append(a)

    dis = [-1] * (n+1)
    dis[1] = 0
    Q = deque()
    Q.append(1)
    while len(Q) >= 1:
        pos = Q.popleft()
        for g in G[pos]:
            if dis[g] == -1:
                dis[g] = dis[pos] + 1
                Q.append(g)

    for i in range(1,n+1):
        print(dis[i])

main()
# 距離確定のタイミング！！