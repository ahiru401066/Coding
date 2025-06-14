def main():
    N,Q = map(int,input().split())
    X = list(map(int,input().split()))

    A = [0] * (Q+1)
    L = [0] * (N+1)
    for i in range(Q):
        if X[i] >= 1:
            L[X[i]] += 1
            A[i+1] = X[i]
        else:
            minBoxIndex = N
            for j in range(N,0,-1):
                if L[minBoxIndex] >= L[j]:
                    minBoxIndex = j
            L[minBoxIndex] += 1
            A[i+1] = minBoxIndex
    
    print(*A[1::])

main()