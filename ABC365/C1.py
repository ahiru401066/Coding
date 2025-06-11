def main():
    def total(x):
        total = sum(min(x,A[i]) for i in range(n))
        return total

    def bfs():
        l = 0
        r = 10**9+1
        while l <= r:
            mid = (l+r)//2
            t = total(mid)
            if t > m: r = mid - 1
            elif t <= m: l = mid + 1
        print(r)

    n,m = map(int,input().split())
    A = list(map(int,input().split()))

    if m >= sum(A):
        print("infinite")
        return
    bfs()

main()
# 単調性