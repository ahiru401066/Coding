def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    count = 0
    p = 0

    for a in A:
        if p + a > K:
            count += 1
            p = 0
        p += a 
    
    if p > 0: count += 1
    print(count)

main()