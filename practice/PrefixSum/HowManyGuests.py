# 累積和の基本
"""要素配列と累積和配列のインデックスの対応に注意"""
def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (len(a)+1)
    for i in range(len(a)):
         s[i+1] = s[i] + a[i]

    for i in range(q):
        l,r = map(int, input().split())
        print(s[r] - s[l-1])

main()