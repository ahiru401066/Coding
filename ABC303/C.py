def main():
    def bs(x,y):
        left = -1; right = M
        while left + 1 < right:
            mid = (left+right)//2
            lx,ly,lz = L[mid]
            if lx == x:
                if ly == y:
                    if lz == 0:
                        L[mid][2] = 1
                        return True
                    else: return False

                elif ly > y: right = mid
                elif ly < y: left = mid

            elif lx > x: right = mid
            elif lx < x: left = mid
        return False

    N,M,H,K = map(int,input().split())
    S = input()
    L = [] #[x,y,0] 最後の要素でアイテムの消費を管理する
    for _ in range(M):
        x,y = map(int,input().split())
        L.append([x,y,0])
    L.sort(key=lambda x:(x[0], x[1]))
    # print(L)

    direction = {"R":(0,1), "L":(0,-1), "U":(1,0), "D":(-1,0)} #(dy,dx)
    pos = [0,0]
    for i in range(N):
        H -= 1
        if H < 0:
            print("No")
            return
        
        dy,dx = direction[S[i]]
        pos[0] += dx; pos[1] += dy

        if H < K:
            if bs(pos[0],pos[1]): H = K
    print("Yes")
    # print(L)

main()
# ２分探索？
# 位置、体力