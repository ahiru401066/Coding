def main():
    H,W = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    print(S)

    direction = [(-1,0),(-1,1),(0,1),]
    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                for d in direction:
                    dy,dx = d
                    if 0 <= x+dx < W and 0 <= y+dy < H:
                        pass

main()
# キュー構造使う？