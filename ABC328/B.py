def main():
    N = int(input())
    D = list(map(int,input().split()))

    ans = 0
    for i in range(N):
        for j in range(1,D[i]+1):
            l = list(str(i+1) + str(j))
            s = set(l)
            if len(s) == 1: ans += 1

    print(ans)

main()