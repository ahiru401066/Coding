import statistics
import math

def main():
    N = int(input())
    R = []; C = []
    for i in range(N):
        r,c = map(int,input().split())
        R.append(r); C.append(c)

    mR = 0
    mC = 0
    mR = statistics.median(R)
    mC = statistics.median(C)
    floorR = math.floor(mR)
    ceilR = math.ceil(mR)
    ceilC = math.ceil(mC)
    floorC = math.floor(mC)

    disR = floorR if max(abs(floorR - r) for r in R) < max(abs(ceilR - r) for r in R) else ceilR
    disC = floorC if max(abs(floorC - c) for c in C) < max(abs(ceilC - c) for c in C) else ceilC
    print(disR,disC)
    if max(abs(r - disR) for r in R) > max(abs(c - disC) for c in C): print(max(abs(r - disR) for r in R))
    else: print(max(abs(c - disC) for c in C))

main()

# 直線 -> 平面
# 収束位置：平均 but, 四捨五入？ <= 考える必要ない？シュミュレーション？