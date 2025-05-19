def main():
    n = int(input())
    P = list(map(int,input().split()))
    rank = [0] * n

    r = 1
    while r <= n:
        k = 0
        # ランクがつけられていない最大値を探す
        maxV = 0
        for i in range(n):
            if rank[i] == 0:
                maxV = max(maxV,P[i])
        # maxV = max(P[i] for i in range(n) if rank[i] == 0)
        
        # 最大値の場合は順位を確定、順位を更新する
        for i in range(n):
            if P[i] == maxV:
                rank[i] = r
                k += 1
        r += k

    for i in range(n):
        print(rank[i])

main()
# 順位と人数を記録
# 順位をつけたかを記録