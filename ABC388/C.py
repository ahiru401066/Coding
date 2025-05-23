def main():
    def binarySearch(l,r,n):
        if A[-1] < n: return -1
        l = l
        r = r
        m = 0
        while(l <= r):
            m = (l+r)//2
            if A[m] >= n: r = m - 1
            elif A[m] < n: l = m + 1
        return l


    n = int(input())
    A = list(map(int,input().split()))
    index = -1
    # B = []
    # for a in A:
    #     if a != index:
    #         B.append(a)
    #     index = a

    count = 0
    for i in range(n):
        x = binarySearch(i+1,n-1,A[i]*2)
        if x == -1: continue
        count += (n-1) - x + 1
    print(count)

main()
# ２分探索使えるはず A[i]* 2以上最小の数