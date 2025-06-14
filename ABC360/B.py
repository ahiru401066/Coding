def main():
    S,T = input().split()

    for i in range(1,len(S)):
        # w文字ごとに区切る
        li = []
        k = 0
        while k < len(S):
            li.append(S[k:k+i])
            k += i
        print(li)   

        # 文字列を縦に見る
        for j in range(len(li[0])):
            txt = ""
            for l in range(len(li)):
                if j > len(li[l])-1:
                    continue
                txt += li[l][j]
            if txt == T:
                print("Yes")
                return

    print("No")

main()
# ２重ループ