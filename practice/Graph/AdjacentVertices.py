# 入力受け取りの練習
def main():
    n,m = map(int, input().split())
    edges = [list(map(int,input().split())) for _ in range(m)]

    G = [list() for _ in range(n+1)]
    for a,b in edges:
        G[a].append(b)
        G[b].append(a)
    
    for i in range(1,len(G)):
        s =": {" + ", ".join([str(e) for e in G[i]]) + "}"
        print(str(i) + s)

main()