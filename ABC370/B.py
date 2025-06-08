def main():
    n = int(input())
    A = [list(map(int,input().split())) for _ in range(n)]
    now = 1
    for i in range(1,n+1):
        if now >= i:
            now = A[now-1][i-1]
        else:
            now = A[i-1][now-1]
    print(now)

main()