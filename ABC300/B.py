def main():
    H,W = map(int,input().split())
    A = [list(input()) for _ in range(H)]
    B = [list(input()) for _ in range(H)]
    # print(A)
    # print(B)

    for dx in range(W):
        for dy in range(H):
            flg = True
            for x in range(W):
                for y in range(H):
                    s = x - dx if x - dx >= 0 else W + (x - dx)
                    t = y - dy if y - dy >= 0 else H + (y - dy)
                    if A[t][s] != B[y][x]:
                        flg = False
            if flg:
                print("Yes")
                return
    print("No")

main()