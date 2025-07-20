def main():
    N,M = map(int,input().split())
    C = list(input().split())
    D = list(input().split())
    P = list(map(int,input().split()))

    dic = {}
    for i in range(M):
        dic[D[i]] = P[i+1]
    # print(dic)
    total = 0
    for i in range(N):
        if not C[i] in dic:
            total += P[0]
        else:
            total += dic[C[i]]
    print(total)

main()