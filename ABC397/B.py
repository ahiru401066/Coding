def main():
    s = input()
    count = insert(s)
    if s[0] == "o" and s[len(s)-1] == "i": count += 2
    elif s[0] == "i" and s[len(s)-1] == "o": count += 0
    else: count += 1
    print(count)

def insert(s): # 文字の挿入数を計算
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]: count += 1
    return count


main()

# i,oが連続しないようにする 文字の連続箇所の数を数える
# 偶奇を考える　先頭文字と文字の長さを確認
