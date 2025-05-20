def main():
    n = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    #人とゼッケン番号のペアを保持 -> ゼッケンを昇順にする
    li = []
    for i in range(n):
        li.append((i,Q[i]))
    li.sort(key=lambda x: x[1])

    # 人から人を探す
    ans = []
    for e in li:
        ans.append(Q[P[e[0]]-1])
    print(*ans)
    
main()
# ゼッケンで人を探す -> 人で人を探す
# ゼッケンで人を探すのはやらないといけないもの