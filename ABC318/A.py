def main():
    N,M,P = map(int,input().split())
    count = 0
    for i in range(1,N+1):
        if i - M >= 0 and (i-M) % P == 0:
            count += 1
    print(count)

main()