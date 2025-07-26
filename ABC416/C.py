def main():
    def dfs(pos,l):
        if l == K:
            A.append(pos)
        else:
            for i in range(N):
                dfs(pos+[i],l+1)

    N,K,X = map(int,input().split())
    S = [input() for _ in range(N)]
    A = []

    dfs([],0)
    # print(A)
    # print(len(A))

    L = []
    for a in A:
        txt = ""
        for e in a:
            txt += S[e]
        L.append(txt)

    L.sort()
    # print(L)
    print(L[X-1])

main()