def main():
    S = input()

    ans = ""
    flg = True
    for i in range(len(S)):
        if flg and S[i] == "|": flg = False; continue
        elif not flg and S[i] == "|": flg = True; continue

        if flg: ans += S[i]
    print(ans)

    # a,b,c = S.split("|")
    # print(a+c)

main()