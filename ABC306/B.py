def main():
    A = list(map(int,input().split()))
    ans = 0
    for i in range(len(A)):
        ans += A[i] * 2**i
    print(ans)

main()