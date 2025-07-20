def main():
    def search(y,x):
        direction = [(-1,-1),(-1,1),(1,-1),(1,1)] #(dy,dx)

        dis = 1
        while True:
            check = ""
            for d in direction:
                dy,dx = d
                dx *= dis; dy *= dis
                if not 0 <= x+dx < W or not 0 <= y + dy < H:
                    check += "."
                else:
                    check += C[y+dy][x+dx]
                
            if check == "####":
                dis += 1
            elif check == "....":
                return dis-1
            else:
                return 0

    H,W = map(int,input().split())
    C = [list(input()) for _ in range(H)]
    L = [0] * (min(H,W)+1)

    for y in range(1,H-1):
        for x in range(1,W-1):
            if C[y][x] == "#":
                result = search(y,x)
                L[result] += 1
    print(*L[1:])

main()