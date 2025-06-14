def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))

    count = 0
    for i in range(N):
        count += H[i]
        if count > M:
            print(i)
            return 
    print(N)

main()