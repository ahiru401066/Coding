def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    l = 1
    r = 10**9
    while(l < r):
        m = (l+r)//2
        ans = check(m,n,k,a)
        if not ans:
            l = m + 1
        else: r = m
    print(l)

def check(x,n,k,a):
    sum = 0
    for i in range(n):
        sum += x//a[i]
    return sum >= k


main()