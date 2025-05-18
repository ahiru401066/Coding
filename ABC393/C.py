def main():
    n,m = map(int,input().split())
    edges = [map(int,input().split()) for _ in range(m)]
    G = [set() for _ in range(n+1)]

    count = 0
    for a, b in edges:
        if a == b:
            count += 1
            continue
        if b in G[a]:
            count += 1
            continue
        G[a].add(b)
        G[b].add(a)
    # print(G)
    print(count)

main()