def main():
    N = int(input())
    A = list(map(int,input().split()))
    K = int(input())
    x = sum(1 for i in range(N) if A[i] >= K)
    print(x)

main()