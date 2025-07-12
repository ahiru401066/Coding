def main():
    A = int(input())
    N = int(input())

    L = [i for i in range(10)]
    LL = [l for l in L]
    flg = True
    while flg:
        for l in L:
            txtBase = str(l)
            for k in range(1,len(L)):
                txt = str(k) + txtBase + str(k)
                if len(txt) > 12:
                    flg = False
                    break
                LL.append(int(txt))

        

main()
# 十進法で絞ってA進法？
# 文字列で絞る？
# 偶奇？