import sys

def main():
    input = sys.stdin.readline  
    N,Q = map(int,input().split())
    S = input()
    Query = [list(map(int,input().split())) for _ in range(Q)]

    L = [0] * (N)
    s = S[0]
    for i in range(N):
        if i == 0: continue
        if S[i] == s:
            L[i] = 1
        else:
            s = S[i]
    
    for i in range(1,N):
        L[i] += L[i-1]

    for query in Query:
        print(L[query[1]-1] - L[query[0]-1])

main()
# 累積和