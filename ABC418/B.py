def main():
    S = input()

    ans = 0.0
    for i in range(len(S)):
        for j in range(i+2,len(S)):
            txt = S[i:j+1]
            c = txt.count("t")
            # print(txt)
            rate = (c - 2) / (len(txt) - 2)
            ans = max(ans,rate)
    print(ans)

main()