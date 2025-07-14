def main():
    N = int(input())
    A = list(map(int,input().split()))
    L = []
    for i in range(N-1):
        s = A[i]
        e = A[i+1]

        if s < e:
            while s < e:
                L.append(s)
                s += 1
        else:
            while s > e:
                L.append(s)
                s -= 1
    else:
        L.append(e)
    print(*L)

main()