from itertools import product

def main():
    N,K,X = map(int,input().split())
    S = [input() for _ in range(N)]

    li = [e for e in range(N)]
    L = list(product(li,repeat=K))
    # print(L)
    SL = []
    for l in L:
        txt = ""
        for e in l:
            txt += S[e]
        SL.append(txt)
    SL.sort()
    # print(SL)
    print(SL[X-1])

main()