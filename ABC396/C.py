def main():
    n,m = map(int,input().split())
    B = list(map(int, input().split()))
    W = list(map(int, input().split()))
    B = sorted(B)
    W = sorted(W)

    preTotalB = []; totalB = 0
    for i in range(len(B)):
        totalB += B[i]
        preTotalB.append(totalB)

    preTotalW = []; totalW = 0
    for i in range(len(W)):
        totalW += W[i]
        preTotalW.append(totalW)

    print(B)
    print(preTotalB)
    print(W)
    print(preTotalW)

    def binarySearch(l,r):
        while(l <= r):
            mid = (l+r)//2
            if 

main()

# 全探索
# 累積和のような考え方？
# 黒と白の累積和をそれぞれ記録？
# 累積和+２分探索？