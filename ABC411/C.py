def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))

    if N == 1:
        for i in range(Q):
            if i % 2 == 0: print(1)
            else: print(0)
        return

    L = [0] * N
    count = 0
    for i in range(Q):
        color = 1 if L[A[i]-1] == 0 else 0
        L[A[i]-1] = color

        if color == 1:
            if A[i]-1 == 0:
                if L[A[i]-1+1] == 0: count += 1
            elif A[i]-1 == N-1:
                if L[A[i]-1-1] == 0: count += 1
            else:
                if L[A[i]-1-1] == 1 and L[A[i]-1+1] == 1: count -= 1
                elif L[A[i]-1-1] == 0 and L[A[i]-1+1] == 0: count += 1
        elif color == 0:
            if A[i]-1 == 0:
                if L[A[i]-1+1] == 0: count -= 1
            elif A[i]-1 == N-1:
                if L[A[i]-1-1] == 0: count -= 1
            else:
                if L[A[i]-1-1] == 1 and L[A[i]-1+1] == 1: count += 1
                elif L[A[i]-1-1] == 0 and L[A[i]-1+1] == 0: count -= 1
        print(count)

main()