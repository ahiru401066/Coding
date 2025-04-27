# ２分探索（値一致　基本）

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    index = binarySearch(a,x)
    return index+1

def binarySearch(li,x):
    l = 0
    r = len(li)-1
    while(True):
        mid = (l+r)//2
        if(x == li[mid]): return mid
        elif(x > li[mid]): l = mid + 1
        elif(x < li[mid]): r = mid - 1
        if l > r: return -1

print(main())