def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    # print(A)
    B = []
    for y in range(N):
        l = []
        for x in range(N):
            # かど
            if x == 0 and y == 0:
                l.append(A[y+1][x])
                continue
            elif x == N-1 and y == 0:
                l.append(A[y][x-1])
                continue
            elif x == 0 and y == N-1:
                l.append(A[y][x+1])
                continue
            elif x == N-1 and y == N-1:
                l.append(A[y-1][x])
                continue

            # 辺
            if y == 0:
                l.append(A[y][x-1])
                continue
            elif y == N-1:
                l.append(A[y][x+1])
                continue
            elif x == 0:
                l.append(A[y+1][x])
                continue
            elif x == N-1:
                l.append(A[y-1][x])
                continue

            l.append(A[y][x])
        B.append(l)
    
    for b in B:
        a = "".join(b)
        print(a)

main()