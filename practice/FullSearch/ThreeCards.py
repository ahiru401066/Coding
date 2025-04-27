def main():
    n,k = map(int, input().split())
    count = 0

    for a in range(1,n+1):
        for b in range(1,n+1):
            c = k - a - b
            if(1 <= c and c <= n): count += 1
    print(count)

main()