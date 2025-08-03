def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(N):
        for j in range(M):
            if A[i] == B[j]:
                A[i] = -1
                B[j] = -1
                continue
    
    print(*[a for a in A if a != -1])

main()