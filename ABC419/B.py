def main():
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]

    L = []
    for q in query:
        c = q[0]
        if c == 1:
            L.append(q[1])
            L.sort(reverse=True)
        else:
            if len(L) == 0: continue
            top = L.pop()
            print(top)

main()