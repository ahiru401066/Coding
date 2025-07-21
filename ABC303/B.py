def main():
    N,M = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(M)]
    S = [set() for _ in range(N)]

    for i in range(M):
        for j in range(N):
            if j-1 >= 0:
                S[A[i][j]-1].add(A[i][j-1])
            
            if j+1 < N:
                S[A[i][j]-1].add(A[i][j+1])
    # print(S)
    total = sum((N-1) - len(s) for s in S)
    print(total//2)

main()