def main():
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        l = []
        for j in range(N):
            if A[i][j] == 1:
                l.append(j+1)
        print(*l)

main()