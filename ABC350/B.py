def main():
    N,Q = map(int,input().split())
    T = list(map(int,input().split()))
    li = [1] * (N+1)
    for i in range(Q):
        if li[T[i]] == 1:
            li[T[i]] -= 1
        else:
            li[T[i]] += 1
    total = sum(1 for i in range(1,N+1) if li[i] == 1)
    print(total)


main()