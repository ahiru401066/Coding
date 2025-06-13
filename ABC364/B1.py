def main():
    h,w = map(int,input().split())
    si,sj = map(int,input().split())
    si -= 1; sj -= 1
    C = [input() for _ in range(h)]
    X = input()

    move = {
        "U": (-1,0),
        "D": (1,0),
        "L": (0,-1),
        "R": (0,1),
    }

    for d in X:
        di, dj = move[d]
        ni,nj = si+di, sj+dj
        if 0 <= ni < h and 0 <= nj < w and C[ni][nj] == ".":
            si,sj = ni,nj
    print(si+1,sj+1)

main()