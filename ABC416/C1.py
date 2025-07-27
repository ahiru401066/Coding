import sys
sys.setrecursionlimit(120000)

def main():
    def dfs(li,l):
        if l == K:
            A.append(li)
            return
        else:
            for i in range(N):
                dfs(li+[i],l+1)

    N,K,X = map(int,input().split())
    S = [input() for _ in range(N)]
    A = []
    dfs([],0)
    # print(A)

    L = []
    for a in A:
        txt = ""
        for e in a:
            txt += S[e]
        L.append(txt)
    L.sort()
    print(L[X-1])

main()