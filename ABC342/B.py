import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    P = list(map(int,input().split()))
    Q = int(input())
    Query = [list(map(int,input().split())) for _ in range(Q)]

    L = [0] * (N+1)
    for i in range(N):
        L[P[i]] = i+1

    for query in Query:
        a,b = query
        p = a if L[a] < L[b] else b
        print(p)

main()