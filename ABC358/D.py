def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()

    j = 0; total = 0
    for i in range(M):
        while j <= len(A)-1:
            if B[i] <= A[j]:
                total += A[j]
                j += 1
                break
            j += 1
        if i != len(B)-1 and j == len(A):
            print(-1)
            return
    print(total)

main()