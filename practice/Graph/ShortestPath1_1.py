from collections import deque

def main():
    n, m = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(m)]
    G = [list() for _ in range(n+1)]
    for a,b in edges:
        G[a].append(b)
        G[b].append(a)
    
    dist = [-1] * (n+1)
    dist[1] = 0
    Q = deque()
    Q.append(1)
    
    while len(Q) >= 1:
        pos = Q.popleft()
        for nex in G[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                Q.append(nex)

    for i in range(1,n+1):
        print(dist[i])


main()