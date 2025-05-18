def main():
    n = int(input())
    A = list(map(int, input().split()))

    B = [] #マスの指示をまとめる
    count = 0
    for e in reversed(A):
        if e == 0: count = 0
        else: count += e
        B.append(count)
    B = [e for e in reversed(B)]
    print(B)



main()
# マスi以上に到達するのに最小回数のサイコロの数を考える
# マスの指示をまとめる？