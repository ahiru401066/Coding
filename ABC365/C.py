import math

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))

    if m >= sum(A):
        print("infinite")
        return

    dic = {}
    for i in range(n):
        if not A[i] in dic.keys():
            dic[A[i]] = 1
        else: dic[A[i]] += 1
    dicKeys = sorted(dic)
    dic = {k:dic[k] for k in dicKeys}

    total = 0; count = 0; ans = 0
    for k,v in dic.items():
        count += v
        total += k * v
        if total + k * (n - count) > m:
            print(k-1)
            return
        else:
            ans = k
    print(ans)

main()
# 一人当たりx ->　合計 <= x*n 
# パターン：予算平均、予算平均+1、inf