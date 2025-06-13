import sys

def main():
    n,x,y = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)

    aTotal = 0; bTotal = 0
    for i in range(n):
        aTotal += A[i]
        bTotal += B[i]
        if aTotal > x or bTotal > y:
            print(i+1)
            return
    print(n)

main()
