import sys

def main():
    input = sys.stdin.readline
    A = []
    Q = int(input())
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            print(A[len(A)-query[1]])

main()