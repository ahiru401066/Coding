def main():
    S = input()

    # それぞれの文字の出現回数カウント
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    li = [0] * len(alphabet)
    for i in range(len(S)):
        for j in range(len(alphabet)):
            if S[i] == alphabet[j]:
                li[j] += 1
    # print(li)

    # 出現回数でまとめる
    L = [list() for i in range(100+1)]
    for i in range(len(li)):
        L[li[i]].append(i+1)
    # print(L)
    
    for i in range(1,len(L)):
        # print(L[i])
        if len(L[i]) != 0 and len(L[i]) != 2:
            print("No")
            return
    print("Yes")

main()
# それぞれの文字が何回現れるかカウントする
