def main():
    M = int(input())
    D = list(map(int,input().split()))

    # if M == 1:
    #     print(1,D[0]//2+1)
    #     return

    mid = sum(D)//2 + 1

    c = 1
    for i in range(M):
        for j in range(1,D[i]+1):
            if c == mid:
                print(i+1,j)
                return
            c += 1

main()