def main():
    n,m = map(int,input().split())
    s = set()
    knightMoves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    for _ in range(m):
        a,b = map(int,input().split())
        s.add((a,b))
        for dx, dy in knightMoves:
            nx, ny = a+dx, b+dy
            if 1 <= nx <= n and 1 <= ny <= n:
                s.add((nx,ny))
    print(n*n - len(s))

main()
#確認　綺麗にコード編集