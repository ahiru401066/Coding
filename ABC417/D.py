def main():
    N = int(input())
    P = [list(map(int,input().split())) for _ in range(N)]
    Q = int(input())
    X = [int(input()) for _ in range(Q)]

    for x in X:
        t = x
        for i in range(N):
            p,a,b = P[i]
            if p >= t: t += a
            elif p < t: t = max(t-b,0)
        print(t)

main()
# テンションが0になったら絶対上がる
# テンションが高いほど下がる可能性が高い