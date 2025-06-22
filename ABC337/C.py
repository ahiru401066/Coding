def main():
    N = int(input())
    A = list(map(int,input().split()))
    L = [0] * (N+2)

    for i in range(N):
        A[i] = 0 if A[i] == -1 else A[i]
        L[A[i]] = i+1
    # print(*L)

    ans = []; pos = 0
    while len(ans) != N:
        ans.append(L[pos])
        pos = L[pos]

    print(*ans)

main()