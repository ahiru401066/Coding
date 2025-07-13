def main():
    A = int(input())
    N = int(input())

    L = []

    # 奇数
    i = 1
    while True:
        s = str(i)
        pal = int(s + s[-2::-1])
        if pal > N:
            break
        L.append(pal)
        i += 1

    # 偶数
    i = 1
    while True:
        s = str(i)
        pal = int(s + s[::-1])
        if pal > N:
            break
        L.append(pal)
        i += 1
    # print(L)
    # print(len(L))

    Z = []
    for l in L:
        x = l
        digits = []
        while x > 0:
            digits.append(x%A)
            x //= A
        if digits == digits[::-1]:
            Z.append(l)
    # print(Z)
    print(sum(Z))

        

main()
# 十進法で絞ってA進法？
# 文字列で絞る？
# 偶奇？