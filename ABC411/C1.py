def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))

    L = [0] * (N+2)
    count = 0
    for a in A:
        before = L[a]

        if before == 0:
            if L[a-1] == 0 and L[a+1] == 0: count += 1
            elif L[a-1] == 1 and L[a+1] == 1: count -= 1
            L[a] = 1
        elif before == 1:
            if L[a-1] == 0 and L[a+1] == 0: count -= 1
            elif L[a-1] == 1 and L[a+1] == 1: count += 1
            L[a] = 0
        print(count)

main()