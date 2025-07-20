def main():
    def bs(n):
        left = -1; right = N
        while left + 1 < right:
            mid = (left+right) // 2
            if A[mid] >= n: right = mid
            else: left = mid 
        return right


    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    LR = []
    for _ in range(Q):
        l,r = map(int,input().split())
        LR.append([l,r])
    
    # 累積和計算
    P = [0] * (N)
    total = 0
    for i in range(1,N):
        if i % 2 == 0:
            total += A[i] - A[i-1]
        P[i] = total
    # print(P)

    for l,r in LR:
        # timeL
        if l == 0:
            timeL = 0
        else:
            nextL = bs(l)
            timeL = P[nextL-1] + (l - A[nextL-1]) if nextL % 2 == 0 else P[nextL-1]

        # timeR
        nextR = bs(r)
        timeR = P[nextR-1] if nextR % 2 != 0 else P[nextR-1] + (r - A[nextR-1])
        
        # print(timeL,timeR)
        print(timeR - timeL)


main()
# 累積和+２分探索