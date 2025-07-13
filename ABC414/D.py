def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))

    X.sort()
    # print(X)

    D = []
    for i in range(len(X)-1):
        D.append(X[i+1]-X[i])
    D.sort()
    # print(D)
    print(sum(D[:(N-M)]))


main()