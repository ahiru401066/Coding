# from collections import OrderedDict

def main():
    def calc(x):
        sumA = sum(1 for a in A if a <= x)
        sumB = sum(1 for b in B if b >= x)
        return sumA >= sumB

    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    left = 0; right = 10**9+1
    while left + 1 < right:
        mid = (left+right)//2
        if calc(mid): right = mid
        else: left = mid
    print(right)

main()