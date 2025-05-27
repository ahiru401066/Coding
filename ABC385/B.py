def main():
    # 入力
    h,w,y,x = map(int,input().split())
    S = [list(input()) for _ in range(h)]
    T = input()

    p = [y-1,x-1]
    # print(S[p[0]][p[1]])
    # print(S[p[0]][p[1]-1])
    count = 0
    for t in T:
        if t == "L" and not S[p[0]][p[1]-1] == "#":
            p[1] -= 1
        elif t == "R" and not S[p[0]][p[1]+1] == "#":
            p[1] += 1
        elif t == "U" and not S[p[0]-1][p[1]] == "#":
            p[0] -= 1
        elif t == "D" and not S[p[0]+1][p[1]] == "#":
            p[0] += 1
        
        if S[p[0]][p[1]] == "@":
            count += 1
            S[p[0]][p[1]] = "*"
    print(p[0]+1,p[1]+1,count)


main()
# データ構造を正しく扱えるか