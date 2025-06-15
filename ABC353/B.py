def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    count = 0
    p = 0
    for i in range(N):
        if p + A[i] <= K:
            p += A[i]
        else:
            count += 1
            p = A[i]
        
        if i == N-1:
            count += 1
    print(count)

main()