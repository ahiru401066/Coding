def main():
    # "/"を検出したときに"11/22"型の文字列の長さを計算する関数
    def check(i):
        l = 1
        while(i-l >= 0 and i+l < n):
            if not (s[i-l] == "1" and s[i+l] == "2"):
                break
            l += 1
        return (l-1) * 2 + 1

    # 入力
    n = int(input())
    s = input()

    m = 0
    for i in range(n):
        if s[i] == "/":
            l = check(i)
            m = max(m,l)
    print(m)



main()
# "/"を探索する -> "/"を検出したら関数で文字数を確認する