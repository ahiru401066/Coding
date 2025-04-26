#累積和
n, k = map(int, input().split())
R = 1000000000

s = k
a = [1] * (n+1)
for i in range(k,n+1):
    a[i] = s
    s -= a[i-k]
    s += a[i]
    s %= R

print(a[n])
