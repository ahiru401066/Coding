def main():
    n, m = map(int, input().split())
    INF = 1000000000
    x = 0
    for i in range(m+1):
        x += n**i
        if x > INF: return "inf"
    return x

print(main())