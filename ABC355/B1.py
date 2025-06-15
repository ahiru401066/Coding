def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    C = A+B
    C.sort()
    flg = False
    for i in range(N+M):
        if i == 0:
            if C[i] in A:
                flg = True
        else:
            if C[i] in A:
                if flg:
                    print("Yes")
                    return
                else: flg = True
            else:
                flg = False
    print("No")

main()