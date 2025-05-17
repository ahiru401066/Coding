def main():
    n = int(input())
    P = list(map(int, input().split()))
    li = [0] * n

    # upとdownの記録
    for i in range(1,n-1):
        if P[i] > P[i+1] and P[i] > P[i-1]: li[i] = 1
        elif P[i] < P[i+1] and P[i] < P[i-1]: li[i] = -1
    print(li)

    # upFlg = False; downFlg = False
    # l = 0; r = 1; index = 0
    # count = 0
    # while(index < n):
    #     if li[index] == -1:
    #         l = index + 1
    #         r = l + 1
    #     if li[index] == 1:

main()
# 多分O(n)だと思うけど、、
# 累積和みたいな？？？
# upとdownをフラグで管理、頭から順にup,downを調べる
# 極大、極小の場所は間違いなく必要
# 虫みたいに進むはず