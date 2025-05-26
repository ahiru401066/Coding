def main():
    n,m = map(int,input().split())
    B = list(map(int, input().split()))
    W = list(map(int, input().split()))

    # Wの累積和を保持
    W = sorted(W,reverse=True)
    cSumW = [0]
    for i in range(len(W)):
        cSumW.append(cSumW[i]+W[i])

    # Bの累積和
    B = sorted(B,reverse=True)
    cSumB = [0]
    for i in range(len(B)):
        cSumB.append(cSumB[i]+B[i])
    # n個以上玉を入れる時の最大値
    t = 0
    for i in range(len(cSumB)-1,0,-1):
        if i == len(cSumB) - 1: continue
        t = cSumB[i+1]
        cSumB[i] = max(cSumB[i],t)

    score = 0
    for i in range(len(cSumW)):
        if i > len(cSumB)-1:
            continue
        score = max(score,cSumW[i] + cSumB[i])
    # print(cSumB)
    # print(cSumW)
    print(score)

main()
# データ保持に対して工夫
# 白の個数が定まったときに黒の個数の候補の中から最大のものを特定できる