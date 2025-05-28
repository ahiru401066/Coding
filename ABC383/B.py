def main():
    # マンハッタン距離内の床の位置を記録する関数
    def count(i,j):
        s = set()
        for k in range(h):
            for l in range(w):
                if S[k][l] == "." and abs(i - k) + abs(j - l) <= d:
                    s.add((k,l))
        return s

    # メイン
    h,w,d = map(int,input().split())
    S = [list(input()) for _ in range(h)]
    setList = []

    for i in range(h):
        for j in range(w):
            if S[i][j] == ".":
                setList.append(count(i,j))

    m = 0
    for i in range(len(setList)):
        for j in range(i+1,len(setList)):
            m = max(m,len(setList[i] | setList[j]))
    print(m)


main()
# 要素の重複はsetを使う