import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    mass = [[0 for _ in range(100)] for _ in range(100)]

    for _ in range(N):
        a,b,c,d = map(int,input().split())
        for y in range(c,d):
            for x in range(a,b):
                mass[y][x] = 1

    ans = 0
    for y in range(100):
        for x in range(100):
            ans += mass[y][x]
    print(ans)

main()