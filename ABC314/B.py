def main():
    N = int(input())
    L = [list() for _ in range(37)]
    C = []; LA = []
    for _ in range(N):
        c = int(input())
        A = list(map(int,input().split()))
        C.append(c); LA.append(A)
    X = int(input())

    for i in range(N):
        for a in LA[i]:
            L[a].append([C[i],i+1])
    # print(*L[X])
    if len(L[X]) == 0:
        print(0)
        return
    
    ans = sorted(L[X],key=lambda x:x[0])
    Z = []
    min = ans[0][0]
    for i in range(len(ans)):
        if ans[i][0] != min:
            break
        Z.append(ans[i][1])
    print(len(Z))
    print(*Z)

main()