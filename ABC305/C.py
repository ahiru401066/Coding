def main():
    H,W = map(int,input().split())
    S = []
    for _ in range(H):
        s = input()
        S.append(s)
    
    X = []
    Y = []
    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                X.append(x)
                Y.append(y)
    # print(X)
    # print(Y)
    minX = min(X); maxX = max(X)
    minY = min(Y); maxY = max(Y)
    # print(minX,minY)
    # print(maxX,maxY)

    for y in range(H):
        for x in range(W):
            if minX <= x <= maxX and minY <= y <= maxY and S[y][x] == ".":
                print(y+1,x+1)
                return

main()