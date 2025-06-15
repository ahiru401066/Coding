def main():
    N,L,R = map(int,input().split())
    ans = []
    mid = []
    for i in range(N):
        if L <= i+1 <= R:
            mid.append(i+1)
        else:
            ans.append(i+1)
    # print(ans)
    # print(mid)
    print(*(ans[:L-1]+ mid[::-1] + ans[L-1::]))


main()
# 逆順を分けて管理、結合
# スライス使うともっと早くかける ex) li[L:R] = li[L:R][-1]