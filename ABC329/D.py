def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    L = [0] * (N+1)

    topIndex = 1
    for a in A:
        L[a] += 1
        if L[a] > L[topIndex]:
            topIndex = a
        elif L[a] == L[topIndex] and a < topIndex:
            topIndex = a
        print(topIndex)

main()