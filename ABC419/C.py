import statistics
import math

def main():
    N = int(input())
    R = []; C = []
    for i in range(N):
        r,c = map(int,input().split())
        R.append(r); C.append(c)

    zR = (max(R) + min(R) + 2 - 1) // 2
    zC = (max(C) + min(C) + 2 - 1) // 2
    
    if zR - min(R) > zC - min(C): print(zR - min(R))
    else: print(zC - min(C))

main()

# 直線 -> 平面
# 収束位置：平均 but, 四捨五入？ <= 考える必要ない？シュミュレーション？
# 収束する場所は最も遠い点たちの移動を軽減する場所！