def main():
    N,Q = map(int,input().split())
    Query = []
    for _ in range(Q):
        line = input().split()
        if line[0] == "1":
            i,p = line
            Query.append((int(i),int(p)))
        elif line[0] == "2":
            i,p,s = line
            Query.append((int(i),int(p),s))
        elif line[0] == "3":
            i,p = line
            Query.append((int(i),int(p)))

    L = ["" for _ in range(N+1)]
    server = ""
    for query in Query:
        if query[0] == 1:
            L[query[1]] = server
        elif query[0] == 2:
            L[query[1]] += query[2]
        elif query[0] == 3:
            server = L[query[1]]
    print(server)

main()