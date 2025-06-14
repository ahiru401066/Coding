import sys

def main():
    n,t,p = map(int,input().split())
    L = list(map(int,input().split()))

    r = 0
    while True:
        count = sum(1 for i in range(n) if L[i] >= t)
        if count >= p:
            print(r)
            break
        else:
            r += 1
            L = [L[i]+1 for i in range(n)]

main()
# 日付記録