import sys

def main():
    input = sys.stdin.readline 
    n = int(input())
    l = 0; tPre = 0
    for i in range(n):
        t,v = map(int,input().split())
        if i == 0:
            tPre = t
        else:
            l = l - (t-tPre) if l-(t-tPre) >= 0 else 0
            tPre = t
        l += v
    print(l)


main()