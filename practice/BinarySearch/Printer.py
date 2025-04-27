# ２分探索（条件を満たす値探索 != 値一致）

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    MAX = 1000_000_000
    result = -1
    
    # binarySearch
    l = 0; r = MAX
    while(l <= r):
        mid = (l+r)//2
        total = check(mid,a)
        if(k > total):
            l = mid + 1
        elif(k <= total):
            result = mid
            r = mid - 1
    return result

def check(t,a):
    total = 0
    for e in a:
        total += t//e
    return total


print(main())