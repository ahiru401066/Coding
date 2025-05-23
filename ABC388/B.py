import sys

def main():
    input = sys.stdin.readline 
    n,d = map(int,input().split())
    T = []; L = []
    for _ in range(n):
        t,l = map(int,input().split())
        T.append(t)
        L.append(l)
    
    for k in range(1,d+1):
        m = 0
        for j in range(n):
            m = max(m, T[j] * (L[j] + k))
        print(m)

main()