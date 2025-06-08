def main():
    s = input()
    t = input()
    s = list(s)
    x = []
    for i in range(len(s)):
        if s[i] != t[i] and s[i] > t[i]:
            s[i] = t[i]
            x.append(s[:])

    for i in range(len(s)-1,-1,-1):
        if s[i] != t[i]:
            s[i] = t[i]
            x.append(s[:])

    print(len(x))
    for e in x:
        print("".join(e))


main()
# 最小の文字配列になるような処理がある
# インデックスが若いものからみていき、修正して文字が小さくなるなら修正を繰り返す
# 1. i:0 -> nで修正を開始
# 2. i:n -> 0で修正を開始