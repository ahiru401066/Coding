def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    G = [list() for _ in range(n+1)]
    for a,b in edges:
        G[a].append(b)
        G[b].append(a)

    print(G)


main()