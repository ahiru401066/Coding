def main():
    N,M,D = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()
    B.sort()
    # print(A)
    # print(B)

    k = 0
    ans = A[0]+B[k] if abs(B[k] - A[0]) <= D else -1
    for i in range(len(A)):
        while True:
            if k+1 >= M:
                if abs(B[k] - A[i]) <= D:
                    ans = max(ans,A[i]+B[k])
                break
            else:
                if abs(B[k] - A[i]) <= D:
                    ans = max(ans,A[i]+B[k])
                if B[k+1] - A[i] > D:
                    break
                k += 1

    print(ans)

main()