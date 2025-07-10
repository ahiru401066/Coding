def main():
    N = int(input())
    maxV = [0] * (N+1)
    maxS = [0] * (N+1)
    for _ in range(N):
        f,s = map(int,input().split())
        if maxV[f] != 0:
            m = maxV[f]+s//2 if maxV[f] >= s else s+maxV[f]//2
            maxS[f] = max(maxS[f],m)
            maxV[f] = max(maxV[f],s)
        else:
            maxV[f] = s

    # print(maxV)
    # print(maxS)
    sameTaste = max(maxS)
    sortedMaxV = sorted(maxV,reverse=True)
    diffTaste = sum(sortedMaxV[0:2])
    if sameTaste > diffTaste: print(sameTaste)
    else: print(diffTaste)



main()
# 同じ味なら２つの最大値と１つの最大値を保持
# 異なる味の種類の最大値をソートして上位２つをたす