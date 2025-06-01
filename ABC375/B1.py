import math

def main():
    n = int(input())
    points = [tuple(map(int,input().split())) for _ in range(n)]
    points = [(0,0)] + points + [(0,0)]

    ans = 0
    for i in range(n+1):
        px,py = points[i]
        qx,qy = points[i+1]
        ans += math.hypot(px-qx,py-qy)
    print(ans)

main()