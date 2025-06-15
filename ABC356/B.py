def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    X = [list(map(int,input().split())) for _ in range(N)]

    L = [0] * M
    for i in range(N):
        for j in range(M):
            L[j] += X[i][j]
    
    for i in range(M):
        if not L[i] >= A[i]:
            print("No")
            return
    print("Yes")

    # for j in range(M):
    #     s = 0
    #     for i in range(N):
    #         s += X[i][j]
    #     if s < A[j]:
    #         print("No")
    #         return
    # print("Yes")


main()
# 全ての品の栄養素を合計 -> 基準を満たすか判定
