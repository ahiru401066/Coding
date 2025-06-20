import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int,input().split()))
    S = []; T = []
    for i in range(N-1):
        s,t = map(int,input().split())
        S.append(s); T.append(t)

    for i in range(N-1):
        A[i+1] += (A[i]//S[i]) * T[i]
    print(A[-1])

main()