def main():
    N,K,X = map(int,input().split())
    A = list(map(int,input().split()))
    li = []
    for i in range(N):
        li.append(A[i])
        if i == K-1:
            li.append(X)
    print(*li)
main()