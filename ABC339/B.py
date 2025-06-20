def main():
    H,W,N = map(int,input().split())
    S = [list("."* W) for _ in range(H)]

    dic = {"up":((1,0,"right"),(-1,0,"left")), "down":((-1,0,"left"),(1,0,"right")), "right":((0,1,"down"),(0,-1,"up")), "left":((0,-1,"up"),(0,1,"down"))}
    x,y = 0,0; direction = "up"
    for _ in range(N):
        if S[y][x] == ".":
            dx,dy,direction = dic[direction][0]
        else:
            dx,dy,direction = dic[direction][1]
        S[y][x] = "#" if S[y][x] == "." else "."
        x,y = (x+dx)%W, (y+dy)%H
    
    for i in range(H):
        ans = ""
        for j in range(W):
            ans += S[i][j]
        print(ans)

main()