def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(len(a)):
        ans += binarySearch(i,a,k)
    print(ans)

def binarySearch(i,li,k):
    x = li[i]
    dis = 0
    index = 0

    l = i+1
    r = len(li)-1
    while(l <= r):
        mid = (l+r)//2
        if(k >= li[mid] - x):
            if (li[mid] - x > dis): 
                dis = li[mid] - x
                index = mid
            l = mid + 1
        elif(k < li[mid] - x): r = mid - 1
    return index-i if(index - i >= 0) else 0

main()