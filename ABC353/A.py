def main():
    N = int(input())
    H = list(map(int,input().split()))
    pre = 0
    for i in range(N):
        if i == 0:
            pre = H[i]
        else:
            if H[i] > pre:
                print(i+1)
                return
    print(-1)

main()