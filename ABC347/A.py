def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = [A[i]//K for i in range(N) if A[i] % K == 0]
    print(*B)

main()