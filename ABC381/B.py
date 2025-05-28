def main():
    s = input()
    keys = list("abcdefghijklmnopqrstuvwxyz")
    dic = {k:0 for k in keys}

    # 文字の長さ確認
    l = len(s)
    if l % 2 != 0:
        print("No"); return
    
    # 連続する２文字の確認とdict要素に保持
    c = ""
    for i in range(len(s)):
        # dicに保持
        dic[s[i]] += 1

        # 連続する２文字の確認
        if i % 2 == 0: c = s[i]
        elif i % 2 != 0:
            if s[i] != c:
                print("No"); return
            c = s[i]
    
    for v in dic.values():
        if not (v == 0 or v == 2):
            print("No"); return
    print("Yes")

main()
# 連続した２つの要素を確認 check 数字変数
# 文字に現れる個数を記録 dict構造