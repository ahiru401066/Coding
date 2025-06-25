import sys

def main():
    input = sys.stdin.readline
    N,S,K = map(int,input().split())
    total = 0
    for _ in range(N):
        p,q = map(int,input().split())
        total += p * q
    if total >= S: print(total)
    else: print(total + K)

main()