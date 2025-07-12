def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]

    for y in range(N-9+1):
        for x in range(M-9+1):
            if S[y][x:x+4] != "###.":
                continue
            if S[y+1][x:x+4] != "###.":
                continue
            if S[y+2][x:x+4] != "###.":
                continue
            if S[y+3][x:x+4] != "....":
                continue
            if S[y+5][x+5:x+9] != "....":
                continue
            if S[y+6][x+5:x+9] != ".###":
                continue
            if S[y+7][x+5:x+9] != ".###":
                continue
            if S[y+8][x+5:x+9] != ".###":
                continue
            print(y+1,x+1)

main()