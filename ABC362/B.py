def main():
    xA,yA = map(int,input().split())
    xB,yB = map(int,input().split())
    xC,yC = map(int,input().split())

    r1_2 = (xA - xB)**2 + (yA - yB)**2
    r2_2 = (xB - xC)**2 + (yB - yC)**2
    r3_2 = (xC - xA)**2 + (yC - yA)**2

    if r1_2 + r2_2 == r3_2 or r2_2 + r3_2 == r1_2 or r3_2 + r1_2 == r2_2:
        print("Yes")
    else: print("No")


main()
# 判定方法は三平方の定理
# ３辺の大小関係から組み合わせを絞る
    # 最も大きい辺を絞る
# ３辺の長さの２乗を求める
