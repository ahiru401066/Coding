def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = "snuke"
    L = len(T)

    # 横
    for y in range(H):
        for x in range(W-L+1):
            txt = S[y][x:x+L]
            if txt == T:
                for k in range(x,x+L):
                    print(y+1,k+1)
                return
            
            if txt[::-1] == T:
                for k in range(x+L-1,x-1,-1):
                    print(y+1,k+1)
                return
    
    # 縦
    for x in range(W):
        for y in range(H-L+1):
            txt = S[y][x] + S[y+1][x] + S[y+2][x] + S[y+3][x] + S[y+4][x]
            if txt == T:
                for k in range(y,y+L):
                    print(k+1,x+1)
                return 
            
            if txt[::-1] == T:
                for k in range(y+L-1,y-1,-1):
                    print(k+1,x+1)
                return
    
    # 右下
    for y in range(H):
        for x in range(W):
            if not 0 <= x+L-1 < W or not 0 <= y+L-1 < H:
                continue
            txt = S[y][x] + S[y+1][x+1] + S[y+2][x+2] + S[y+3][x+3] + S[y+4][x+4]
            if txt == T:
                for k in range(L):
                    print(y+k+1,x+k+1)
                return
            
            if txt[::-1] == T:
                for k in range(L-1,-1,-1):
                    print(y+k+1,x+k+1)
                return
    
    # 右上
    for y in range(H):
        for x in range(W):
            if not 0 <= x-L+1 < W or not 0 <= y+L-1 < H:
                continue
            txt = S[y][x] + S[y+1][x-1] + S[y+2][x-2] + S[y+3][x-3] + S[y+4][x-4]
            if txt == T:
                for k in range(L):
                    print(y+k+1,x-k+1)
                return
            
            if txt[::-1] == T:
                for k in range(L-1,-1,-1):
                    print(y+k+1,x-k+1)
                return

main()
# 全探索　縦、横、斜め（右上、右下）