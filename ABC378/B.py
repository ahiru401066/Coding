import sys

def main():
    input = sys.stdin.readline 
    n = int(input())
    Q = [0] * (n+1)
    R = [0] * (n+1)
    for i in range(1,n+1):
        q,r = map(int,input().split())
        Q[i] = q; R[i] = r
    
    T = []; D = []
    m = int(input())
    for i in range(m):
        t,d = map(int,input().split())
        T.append(t); D.append(d)

    for i in range(m):
        d = D[i]; t = T[i]
        x = d + calc(Q[t],R[t],d%Q[t])
        print(x) 

def calc(a,b,c):
    if b >= c: return b - c
    else:
        return (a-c) + b

main()
# 問題文ややこしい