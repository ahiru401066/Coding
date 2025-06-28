def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    
    L = [1] * (N+1)
    for i in range(M):
        L[A[i]] = 0

    pre = N-1
    for i in range(N,-1,-1):
        if L[i] == 0: pre = i
        else:
            L[i] = pre - i

    for i in range(1,N+1):
        print(L[i])
        

main()