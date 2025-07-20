from collections import deque

def main():
    N,D = map(int,input().split())
    X = []; Y = []
    for _ in range(N):
        x,y = map(int,input().split())
        X.append(x); Y.append(y)
    L = [list() for _ in range(N)]

    # 各点の繋がりを記録
    for i in range(N):
        for j in range(i+1,N):
            if (X[i] - X[j])**2 + (Y[i] - Y[j])**2 <= D**2:
                L[i].append(j)
                L[j].append(i)
    # print(L)

    # 幅優先探索
    Q = deque()
    visited = [False] * (N)
    pos = 0; visited[pos] = True
    Q.append(pos)

    while len(Q) != 0:
        head = Q.popleft()
        for v in L[head]:
            if not visited[v]:
                visited[v] = True
                Q.append(v)
    
    for v in visited:
        if v: print("Yes")
        else: print("No")

main()
# グラフっぽい...