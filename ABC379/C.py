def main():
    n, m = map(int,input().split())
    X = list(map(int,input().split()))
    A = list(map(int,input().split()))

    count = 0
    for i in range(len(X)):
        if i == len(X)-1:
            if X[i] == n:
                if A[i] != 1: print(-1); return
                else: print(count); return
            continue
        d = X[i+1] - X[i]
        if A[i] < d: print(-1); return
        else:
            A[i+1] += A[i] - (d-1) - 1
            # count += d * (d-1)//2 + d * (A[i] - (d-1) - 1)
            count += d*(d+1)//2 - d + d * (A[i] - (d-1) - 1)
    if A[-1] != 1:print(-1)
    else: print(count)

main()
# 小さいマスから操作する
# シュミレーション