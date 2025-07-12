def main():
    N,P,Q = map(int,input().split())
    D = list(map(int,input().split()))
    m = min(D)
    if P >= m+Q:
        print(m+Q)
    else:
        print(P)

main()