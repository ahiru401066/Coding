def main():
    N = int(input())
    D = list(map(int,input().split()))
    for i in range(N-1):
        li = []; d = 0
        for j in range(i,N-1):
            d += D[j]
            li.append(d)
        print(*li)

main()