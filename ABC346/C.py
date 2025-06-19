def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    B = [A[i] for i in range(N) if 1 <= A[i] <= K]
    s = set(B)
    total = K*(K+1)//2
    print(total - sum(s))

main()